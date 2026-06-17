from django.http import Http404
from django.shortcuts import render
from .models import (
    SwierkappKierunek, SwierkappStudia, SwierkappPrzedmiot,
    SwierkappKarta, SwierkappPrzedmiotKoordynatorzy, SwierkappKartaProwadzacy,
)


def _build_faculties():
    STOPIEN_MAP = {
        'I': 'Studia inżynierskie I stopnia',
        'II': 'Studia magisterskie II stopnia',
        'podypl.': 'Studia podyplomowe',
    }
    STOPIEN_BADGE = {
        'I': 'I stopień',
        'II': 'II stopień',
        'podypl.': 'Podyplomowe',
    }
    FORMA_MAP = {
        'st.': 'Stacjonarne',
        'niest.': 'Niestacjonarne',
    }

    faculties = []
    for kierunek in SwierkappKierunek.objects.all():
        if kierunek.name == 'no english name yet !':
            continue

        studia_list = SwierkappStudia.objects.filter(
            kierunek=kierunek
        ).select_related('specjalnosc')

        programs = []
        for studia in studia_list:
            stopien = STOPIEN_MAP.get(studia.stopien, studia.stopien)
            forma = FORMA_MAP.get(studia.forma or '', studia.forma or 'Stacjonarne')
            specjalnosc = studia.specjalnosc.nazwa if studia.specjalnosc.nazwa != '---' else ''

            if specjalnosc:
                title = f'{kierunek.nazwa}, spec. {specjalnosc}'
            else:
                title = kierunek.nazwa

            detail = f'{stopien}, {forma}'
            description = f'{title} – {studia.liczba_semestrow} semestrów'

            semesters = _build_semesters(studia)
            programs.append({
                'title': title,
                'slug': str(studia.id),
                'detail': detail,
                'description': description,
                'semesters': semesters,
                'stopien': studia.stopien,
                'stopien_badge': STOPIEN_BADGE.get(studia.stopien, studia.stopien),
                'forma': studia.forma or 'st.',
                'forma_badge': FORMA_MAP.get(studia.forma or '', 'Stacjonarne'),
            })

        faculties.append({
            'slug': str(kierunek.id),
            'name': kierunek.nazwa,
            'description': f'Kierunek: {kierunek.nazwa}',  # change this
            'programs': programs,
        })
    return faculties


def _build_semesters(studia):
    from .models import SwierkappCykl

    # Get the most recent non-abstract cykl for this studia
    cykl = SwierkappCykl.objects.filter(
        studia=studia,
        abstrakcyjny=False,
        publiczne=True,
    ).order_by('-poczatek__rok_akademicki').first()

    if not cykl:
        return []

    przedmioty = SwierkappPrzedmiot.objects.filter(
        cykl=cykl
    ).select_related('nazwa', 'kategoria').order_by('sem', 'nazwa__nazwa')

    SPECIAL_SEMESTERS = {
        100: 'Przedmioty do wyboru',
        400: 'Przedmioty dodatkowe',
    }

    semesters_dict = {}
    for p in przedmioty:
        sem_nr = p.sem
        if sem_nr not in semesters_dict:
            semesters_dict[sem_nr] = []
        hours = f'{p.liczba_godzin_w}W, {p.liczba_godzin_c}C, {p.liczba_godzin_l}L, {p.liczba_godzin_p}P'
        semesters_dict[sem_nr].append({
            'id': p.id,
            'name': p.nazwa.nazwa,
            'hours': hours,
            'ects': p.ects,
            'form': 'Egzamin' if p.egzamin else 'Zaliczenie',
            'obligatory': 'Obowiązkowy',
        })

    semesters = []
    for sem_nr in sorted(semesters_dict.keys()):
        subjects = semesters_dict[sem_nr]
        name = SPECIAL_SEMESTERS.get(sem_nr, f'Semestr {sem_nr}')
        semesters.append({
            'name': name,
            'content': '',
            'subjects': subjects,
            'total_ects': sum(s['ects'] for s in subjects),
            'total_hours': None,
        })
    return semesters


def index(request):
    faculties = _build_faculties()
    total_programs = sum(len(f['programs']) for f in faculties)
    programs = [
        {'title': 'Studia inżynierskie I stopnia', 'description': 'Programy kształcenia obejmujące podstawy informatyki, automatyki oraz inżynierii.', 'level': '1. stopień'},
        {'title': 'Studia magisterskie II stopnia', 'description': 'Sylabusy dla kierunków technicznych i menedżerskich z naciskiem na praktyczne projekty.', 'level': '2. stopień'},
        {'title': 'Studia podyplomowe', 'description': 'Kursy specjalistyczne dla profesjonalistów i absolwentów szukających rozwoju.', 'level': 'Podyplomowe'},
    ]
    return render(request, 'sylabusy/index.html', {
        'programs': programs,
        'faculties': faculties,
        'total_programs': total_programs,
        'total_faculties': len(faculties),
        'university': 'Politechnika Białostocka',
    })


def faculty_detail(request, slug):
    faculty = next((f for f in _build_faculties() if f['slug'] == slug), None)
    if not faculty:
        raise Http404('Wydział nie znaleziony')
    return render(request, 'sylabusy/faculty.html', {
        'faculty': faculty,
        'university': 'Politechnika Białostocka',
    })


def program_detail(request, faculty_slug, program_slug):
    faculty = next((f for f in _build_faculties() if f['slug'] == faculty_slug), None)
    if not faculty:
        raise Http404('Wydział nie znaleziony')
    program = next((p for p in faculty['programs'] if p['slug'] == program_slug), None)
    if not program:
        raise Http404('Kierunek nie znaleziony')
    return render(request, 'sylabusy/program.html', {
        'faculty': faculty,
        'program': program,
        'university': 'Politechnika Białostocka',
    })


def subject_detail(request, faculty_slug, program_slug, przedmiot_id):
    faculty = next((f for f in _build_faculties() if f['slug'] == faculty_slug), None)
    if not faculty:
        raise Http404('Wydział nie znaleziony')
    program = next((p for p in faculty['programs'] if p['slug'] == program_slug), None)
    if not program:
        raise Http404('Kierunek nie znaleziony')

    try:
        p = SwierkappPrzedmiot.objects.select_related(
            'nazwa', 'jednostka', 'kategoria', 'cykl', 'cykl__studia',
            'cykl__studia__kierunek', 'cykl__studia__specjalnosc',
        ).get(id=przedmiot_id)
    except SwierkappPrzedmiot.DoesNotExist:
        raise Http404('Przedmiot nie znaleziony')

    STOPIEN_MAP = {
        'I': 'Studia inżynierskie I stopnia',
        'II': 'Studia magisterskie II stopnia',
        'podypl.': 'Studia podyplomowe',
    }
    FORMA_MAP = {
        'st.': 'Stacjonarne',
        'niest.': 'Niestacjonarne',
    }

    studia = p.cykl.studia
    stopien = STOPIEN_MAP.get(studia.stopien, studia.stopien)
    forma = FORMA_MAP.get(studia.forma or '', studia.forma or 'Stacjonarne')
    specjalnosc = studia.specjalnosc.nazwa if studia.specjalnosc.nazwa != '---' else '-'

    koordynatorzy = SwierkappPrzedmiotKoordynatorzy.objects.filter(
        przedmiot=p
    ).select_related('user')
    koordynator_names = ', '.join(
        f'{k.user.first_name} {k.user.last_name}'.strip()
        for k in koordynatorzy
    ) or '-'

    prowadzacy_names = '-'
    karta = None
    try:
        karta = SwierkappKarta.objects.get(przedmiot=p)
        prowadzacy = SwierkappKartaProwadzacy.objects.filter(
            karta=karta
        ).select_related('user')
        prowadzacy_names = ', '.join(
            f'{pr.user.first_name} {pr.user.last_name}'.strip()
            for pr in prowadzacy
        ) or '-'
    except SwierkappKarta.DoesNotExist:
        pass

    godziny = []
    if p.liczba_godzin_w:
        godziny.append(f'Wykład: {p.liczba_godzin_w}')
    if p.liczba_godzin_c:
        godziny.append(f'Ćwiczenia audytoryjne: {p.liczba_godzin_c}')
    if p.liczba_godzin_l:
        godziny.append(f'Laboratorium: {p.liczba_godzin_l}')
    if p.liczba_godzin_p:
        godziny.append(f'Projekt: {p.liczba_godzin_p}')
    if p.liczba_godzin_ps:
        godziny.append(f'Praktyka/seminarium: {p.liczba_godzin_ps}')
    if p.liczba_godzin_s:
        godziny.append(f'Seminarium: {p.liczba_godzin_s}')

    subject = {
        'nazwa': p.nazwa.nazwa,
        'kierunek': studia.kierunek.nazwa,
        'specjalnosc': specjalnosc,
        'jednostka': p.jednostka.nazwa if p.jednostka else '-',
        'poziom': stopien,
        'forma': forma,
        'profil': studia.profil or 'Ogólnoakademicki',
        'cykl': p.cykl.opis,
        'kod': p.kod,
        'obligatoryjnosc': 'Obowiązkowy',
        'blok': p.kategoria.nazwa if p.kategoria else '-',
        'koordynator': koordynator_names,
        'prowadzacy': prowadzacy_names,
        'semestr': p.sem,
        'forma_zaliczenia': 'Egzamin' if p.egzamin else 'Zaliczenie',
        'godziny': godziny,
        'ects': p.ects,
        'zalozenia': karta.zalozenia if karta else p.zalozenia,
        'tresci': karta.tresci if karta else p.tresci_ramowe,
        'literatura_podstawowa': karta.literatura_podstawowa if karta else '',
        'literatura_uzupelniajaca': karta.literatura_uzupelniajaca if karta else '',
    }

    return render(request, 'sylabusy/subject.html', {
        'faculty': faculty,
        'program': program,
        'subject': subject,
        'university': 'Politechnika Białostocka',
    })