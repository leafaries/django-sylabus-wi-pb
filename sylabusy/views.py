from django.http import Http404
from django.shortcuts import render

FACULTIES = [
    {
        'slug': 'wydzial-informatyki-elektroniki-i-telekomunikacji',
        'name': 'Wydział Informatyki, Elektroniki i Telekomunikacji',
        'description': 'Technologie informatyczne, telekomunikacyjne i systemy elektroniczne.',
        'programs': [
            {
                'title': 'Informatyka',
                'slug': 'informatyka',
                'detail': 'Studia inżynierskie I stopnia, Stacjonarne',
                'description': 'Kierunek Informatyka koncentruje się na programowaniu, algorytmice, systemach sieciowych oraz technologii chmurowej.',
                'semesters': [
                    {
                        'name': 'Semestr 1',
                        'content': 'Podstawy programowania, algebra liniowa, wprowadzenie do informatyki.',
                        'total_hours': 400,
                        'total_ects': 30,
                        'subjects': [
                            {'name': 'Podstawy programowania', 'hours': '30 wykład, 45 pracownia specjalistyczna', 'ects': 6, 'form': 'Egzamin', 'obligatory': 'Obowiązkowy'},
                            {'name': 'Algebra liniowa z geometrią analityczną', 'hours': '30 wykład, 20 ćwiczenia, 15 pracownia specjalistyczna', 'ects': 5, 'form': 'Egzamin', 'obligatory': 'Obowiązkowy'},
                            {'name': 'Analiza matematyczna', 'hours': '30 wykład, 20 ćwiczenia, 15 pracownia specjalistyczna', 'ects': 5, 'form': 'Egzamin', 'obligatory': 'Obowiązkowy'},
                            {'name': 'Fizyka dla informatyków', 'hours': '30 wykład, 30 ćwiczenia', 'ects': 4, 'form': 'Zaliczenie', 'obligatory': 'Obowiązkowy'},
                            {'name': 'Wprowadzenie do systemu Linux', 'hours': '20 wykład, 30 pracownia specjalistyczna', 'ects': 4, 'form': 'Zaliczenie', 'obligatory': 'Obowiązkowy'},
                            {'name': 'Wprowadzenie do informatyki', 'hours': '30 wykład, 15 ćwiczenia', 'ects': 3, 'form': 'Zaliczenie', 'obligatory': 'Obowiązkowy'},
                            {'name': 'Logika dla informatyków', 'hours': '15 wykład, 15 ćwiczenia', 'ects': 2, 'form': 'Zaliczenie', 'obligatory': 'Obowiązkowy'},
                            {'name': 'Metodyka studiowania (HES I)', 'hours': '10 zajęcia', 'ects': 1, 'form': 'Zaliczenie', 'obligatory': 'Obowiązkowy'},
                        ]
                    },
                    {'name': 'Semestr 2', 'content': 'Struktury danych i algorytmy, bazy danych, architektura komputerów.'},
                    {'name': 'Semestr 3', 'content': 'Systemy operacyjne, inżynieria oprogramowania, sieci komputerowe.'},
                    {'name': 'Semestr 4', 'content': 'Bazy danych zaawansowane, programowanie obiektowe, bezpieczeństwo IT.'},
                    {'name': 'Semestr 5', 'content': 'Sztuczna inteligencja, automatyka, technologie webowe.'},
                    {'name': 'Semestr 6', 'content': 'Praca zespołowa, projekt, analiza danych, testowanie i wdrażanie systemów.'},
                    {'name': 'Semestr 7', 'content': 'Przygotowanie do obrony pracy dyplomowej i praktyka zawodowa.'},
                ],
            },
            {
                'title': 'Data Science',
                'slug': 'data-science',
                'detail': 'Studia magisterskie inżynierskie II stopnia, Stacjonarne',
                'description': 'Data Science uczy analizy danych, uczenia maszynowego i budowy modeli predykcyjnych.',
                'semesters': [
                    {'name': 'Semestr 1', 'content': 'Statystyka, programowanie w Pythonie, wprowadzenie do uczenia maszynowego.'},
                    {'name': 'Semestr 2', 'content': 'Bazy danych, eksploracja danych, modelowanie probabilistyczne.'},
                    {'name': 'Semestr 3', 'content': 'Uczenie głębokie, analiza tekstu, wizualizacja danych.'},
                    {'name': 'Semestr 4', 'content': 'Projekt magisterski, systemy rekomendacyjne, etyka analizy danych.'},
                ],
            },
            {
                'title': 'Matematyka stosowana, spec. Matematyka nowoczesnych technologii',
                'slug': 'matematyka-nowoczesnych-technologii',
                'detail': 'Studia inżynierskie I stopnia, Stacjonarne',
                'description': 'Matematyka stosowana przygotowuje do pracy z modelami matematycznymi i technologiami cyfrowymi.',
                'semesters': [
                    {'name': 'Semestr 1', 'content': 'Analiza matematyczna, algebra, programowanie numeryczne.'},
                    {'name': 'Semestr 2', 'content': 'Równania różniczkowe, statystyka, obliczenia naukowe.'},
                    {'name': 'Semestr 3', 'content': 'Metody numeryczne, modelowanie procesów, ekonometria.'},
                    {'name': 'Semestr 4', 'content': 'Optymalizacja, teoria grafów, analiza sygnałów.'},
                    {'name': 'Semestr 5', 'content': 'Zastosowania AI, analiza danych, modelowanie finansowe.'},
                    {'name': 'Semestr 6', 'content': 'Projekt zespołowy, zastosowanie matematyki w technologii.'},
                    {'name': 'Semestr 7', 'content': 'Przygotowanie do pracy dyplomowej, praktyka i warsztaty.'},
                ],
            },
            {
                'title': 'Matematyka stosowana, spec. Analityka danych',
                'slug': 'matematyka-analityka-danych',
                'detail': 'Studia inżynierskie I stopnia, Stacjonarne',
                'description': 'Program łączy matematykę z analizą danych, statystyką i modelowaniem biznesowym.',
                'semesters': [
                    {'name': 'Semestr 1', 'content': 'Analiza matematyczna, algebra, statystyka w danych.'},
                    {'name': 'Semestr 2', 'content': 'Rachunek prawdopodobieństwa, programowanie w Pythonie, analiza danych.'},
                    {'name': 'Semestr 3', 'content': 'Bazy danych, modele statystyczne, wizualizacja danych.'},
                    {'name': 'Semestr 4', 'content': 'Uczenie maszynowe, przetwarzanie danych, analiza ekonomiczna.'},
                    {'name': 'Semestr 5', 'content': 'Analiza wielowymiarowa, dane przestrzenne, zbiór danych w praktyce.'},
                    {'name': 'Semestr 6', 'content': 'Projekt zespołowy, analiza biznesowa, praktyka w analityce danych.'},
                    {'name': 'Semestr 7', 'content': 'Przygotowanie pracy dyplomowej i praktyczne case study.'},
                ],
            },
            {
                'title': 'Informatyka i Ekonometria',
                'slug': 'informatyka-i-ekonometria',
                'detail': 'Studia magisterskie II stopnia, Stacjonarne',
                'description': 'Kierunek łączy technologie informatyczne z modelami ekonometrycznymi i analizą ekonomiczną.',
                'semesters': [
                    {'name': 'Semestr 1', 'content': 'Ekonometria, analiza danych, programowanie zaawansowane.'},
                    {'name': 'Semestr 2', 'content': 'Modele ekonometryczne, big data, uczenie maszynowe.'},
                    {'name': 'Semestr 3', 'content': 'Modelowanie finansowe, prognozowanie, wizualizacja danych.'},
                    {'name': 'Semestr 4', 'content': 'Projekt magisterski, praktyka i zastosowania w biznesie.'},
                ],
            },
        ],
    },
    {
        'slug': 'wydzial-inzynierii-mechanicznej',
        'name': 'Wydział Inżynierii Mechanicznej',
        'description': 'Kierunki techniczne związane z projektowaniem maszyn i robotyką.',
        'programs': [
            {
                'title': 'Inżynieria mechaniczna',
                'slug': 'inzynieria-mechaniczna',
                'detail': 'Studia inżynierskie I stopnia, Stacjonarne',
                'description': 'Kierunek koncentruje się na projektowaniu maszyn, materiałach i systemach napędowych.',
                'semesters': [
                    {'name': 'Semestr 1', 'content': 'Fizyka techniczna, mechanika ogólna, CAD.'},
                    {'name': 'Semestr 2', 'content': 'Wytrzymałość materiałów, termodynamika, rysunek techniczny.'},
                ],
            },
        ],
    },
    {
        'slug': 'wydzial-architektury',
        'name': 'Wydział Architektury',
        'description': 'Programy związane z projektowaniem przestrzeni i architekturą.',
        'programs': [
            {
                'title': 'Architektura',
                'slug': 'architektura',
                'detail': 'Studia inżynierskie I stopnia, Stacjonarne',
                'description': 'Studia skupiają się na projektowaniu przestrzeni, materiałach i budownictwie.',
                'semesters': [
                    {'name': 'Semestr 1', 'content': 'Wprowadzenie do architektury, rysunek, historia architektury.'},
                    {'name': 'Semestr 2', 'content': 'Projektowanie, materiały budowlane, konstrukcje.'},
                ],
            },
        ],
    },
]


def index(request):
    programs = [
        {
            'title': 'Studia inżynierskie I stopnia',
            'description': 'Programy kształcenia obejmujące podstawy informatyki, automatyki oraz inżynierii.',
            'level': '1. stopień',
        },
        {
            'title': 'Studia magisterskie II stopnia',
            'description': 'Sylabusy dla kierunków technicznych i menedżerskich z naciskiem na praktyczne projekty.',
            'level': '2. stopień',
        },
        {
            'title': 'Studia podyplomowe',
            'description': 'Kursy specjalistyczne dla profesjonalistów i absolwentów szukających rozwoju.',
            'level': 'Podyplomowe',
        },
    ]
    context = {
        'programs': programs,
        'faculties': FACULTIES,
        'university': 'Politechnika Białostocka',
    }
    return render(request, 'sylabusy/index.html', context)


def faculty_detail(request, slug):
    faculty = next((item for item in FACULTIES if item['slug'] == slug), None)
    if not faculty:
        raise Http404('Wydział nie znaleziony')

    context = {
        'faculty': faculty,
        'university': 'Politechnika Białostocka',
    }
    return render(request, 'sylabusy/faculty.html', context)


def program_detail(request, faculty_slug, program_slug):
    faculty = next((item for item in FACULTIES if item['slug'] == faculty_slug), None)
    if not faculty:
        raise Http404('Wydział nie znaleziony')

    program = next((item for item in faculty['programs'] if item['slug'] == program_slug), None)
    if not program:
        raise Http404('Kierunek nie znaleziony')

    context = {
        'faculty': faculty,
        'program': program,
        'university': 'Politechnika Białostocka',
    }
    return render(request, 'sylabusy/program.html', context)
