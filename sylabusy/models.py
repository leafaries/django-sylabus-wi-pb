# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class SwierkappCykl(models.Model):
    id = models.BigAutoField(primary_key=True)
    publiczne = models.BooleanField()
    edytowalne = models.BooleanField()
    opis = models.TextField()
    desc = models.TextField()
    abstrakcyjny = models.BooleanField()
    szablon_karty = models.CharField(max_length=128)
    cykl_nadrzedny = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    grupa_efektow_kierunkowych = models.ForeignKey('SwierkappGrupaefektowkierunkowych', models.DO_NOTHING)
    koniec = models.ForeignKey('SwierkappSemestr', models.DO_NOTHING)
    poczatek = models.ForeignKey('SwierkappSemestr', models.DO_NOTHING, related_name='swierkappcykl_poczatek_set')
    studia = models.ForeignKey('SwierkappStudia', models.DO_NOTHING)
    prk = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Swierkapp_cykl'


class SwierkappCyklAdministratorzy(models.Model):
    id = models.BigAutoField(primary_key=True)
    cykl = models.ForeignKey(SwierkappCykl, models.DO_NOTHING)
    user = models.ForeignKey('SwierkappUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Swierkapp_cykl_administratorzy'
        unique_together = (('cykl', 'user'),)


class SwierkappDyscyplina(models.Model):
    id = models.BigAutoField(primary_key=True)
    nazwa = models.CharField(unique=True, max_length=128)
    name = models.CharField(max_length=128)
    dziedzina = models.ForeignKey('SwierkappDziedzina', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Swierkapp_dyscyplina'


class SwierkappDziedzina(models.Model):
    id = models.BigAutoField(primary_key=True)
    nazwa = models.CharField(unique=True, max_length=128)
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'Swierkapp_dziedzina'


class SwierkappEfektkierunkowy(models.Model):
    id = models.BigAutoField(primary_key=True)
    symbol = models.CharField(max_length=32)
    opis = models.TextField()
    desc = models.TextField()
    rodzaj = models.CharField(max_length=2)
    edytowalne = models.BooleanField()
    dyscyplina = models.ForeignKey(SwierkappDyscyplina, models.DO_NOTHING, blank=True, null=True)
    grupa = models.ForeignKey('SwierkappGrupaefektowkierunkowych', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Swierkapp_efektkierunkowy'


class SwierkappEfektkierunkowyEfektyObszarowe(models.Model):
    id = models.BigAutoField(primary_key=True)
    efektkierunkowy = models.ForeignKey(SwierkappEfektkierunkowy, models.DO_NOTHING)
    efektobszarowy = models.ForeignKey('SwierkappEfektobszarowy', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Swierkapp_efektkierunkowy_efekty_obszarowe'
        unique_together = (('efektkierunkowy', 'efektobszarowy'),)


class SwierkappEfektobszarowy(models.Model):
    id = models.BigAutoField(primary_key=True)
    symbol = models.CharField(max_length=16)
    opis = models.TextField()
    desc = models.TextField()
    rodzaj = models.CharField(max_length=2)
    grupa = models.ForeignKey('SwierkappGrupaefektowobszarowych', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Swierkapp_efektobszarowy'


class SwierkappEfektprzedmiotowy(models.Model):
    id = models.BigAutoField(primary_key=True)
    symbol = models.CharField(max_length=32)
    opis = models.TextField()
    desc = models.TextField()
    metoda_weryfikacji = models.TextField()
    verification_method = models.TextField()
    forma_metody_weryfikacji = models.TextField()
    class_form = models.TextField()
    publiczne = models.BooleanField()
    edytowalne = models.BooleanField()
    karta = models.ForeignKey('SwierkappKarta', models.DO_NOTHING)
    rodzaj = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Swierkapp_efektprzedmiotowy'


class SwierkappEfektprzedmiotowyEfektyKierunkowe(models.Model):
    id = models.BigAutoField(primary_key=True)
    efektprzedmiotowy = models.ForeignKey(SwierkappEfektprzedmiotowy, models.DO_NOTHING)
    efektkierunkowy = models.ForeignKey(SwierkappEfektkierunkowy, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Swierkapp_efektprzedmiotowy_efekty_kierunkowe'
        unique_together = (('efektprzedmiotowy', 'efektkierunkowy'),)


class SwierkappGrupaefektowkierunkowych(models.Model):
    id = models.BigAutoField(primary_key=True)
    data_od = models.DateField()
    opis = models.TextField()
    desc = models.TextField()
    publiczne = models.BooleanField()
    edytowalne = models.BooleanField()
    dyscyplina_wiodaca = models.ForeignKey(SwierkappDyscyplina, models.DO_NOTHING, blank=True, null=True)
    grupa_efektow_obszarowych = models.ForeignKey('SwierkappGrupaefektowobszarowych', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Swierkapp_grupaefektowkierunkowych'


class SwierkappGrupaefektowkierunkowychAdministratorzy(models.Model):
    id = models.BigAutoField(primary_key=True)
    grupaefektowkierunkowych = models.ForeignKey(SwierkappGrupaefektowkierunkowych, models.DO_NOTHING)
    user = models.ForeignKey('SwierkappUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Swierkapp_grupaefektowkierunkowych_administratorzy'
        unique_together = (('grupaefektowkierunkowych', 'user'),)


class SwierkappGrupaefektowkierunkowychInneDyscypliny(models.Model):
    id = models.BigAutoField(primary_key=True)
    grupaefektowkierunkowych = models.ForeignKey(SwierkappGrupaefektowkierunkowych, models.DO_NOTHING)
    dyscyplina = models.ForeignKey(SwierkappDyscyplina, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Swierkapp_grupaefektowkierunkowych_inne_dyscypliny'
        unique_together = (('grupaefektowkierunkowych', 'dyscyplina'),)


class SwierkappGrupaefektowobszarowych(models.Model):
    id = models.BigAutoField(primary_key=True)
    data_od = models.DateField()
    opis = models.TextField()
    desc = models.TextField()

    class Meta:
        managed = False
        db_table = 'Swierkapp_grupaefektowobszarowych'


class SwierkappGrupaefektowobszarowychAdministratorzy(models.Model):
    id = models.BigAutoField(primary_key=True)
    grupaefektowobszarowych = models.ForeignKey(SwierkappGrupaefektowobszarowych, models.DO_NOTHING)
    user = models.ForeignKey('SwierkappUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Swierkapp_grupaefektowobszarowych_administratorzy'
        unique_together = (('grupaefektowobszarowych', 'user'),)


class SwierkappJednostka(models.Model):
    id = models.BigAutoField(primary_key=True)
    nazwa = models.CharField(unique=True, max_length=128)
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'Swierkapp_jednostka'


class SwierkappKarta(models.Model):
    id = models.BigAutoField(primary_key=True)
    zalozenia = models.TextField()
    goals = models.TextField()
    zaliczenie = models.TextField()
    evaluation_form = models.TextField()
    tresci = models.TextField()
    content = models.TextField()
    godziny_kontaktowe = models.CharField(max_length=64)
    godziny_kontaktowe_ects = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    godziny_praktyczne = models.CharField(max_length=64)
    godziny_praktyczne_ects = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    literatura_podstawowa = models.TextField()
    literatura_uzupelniajaca = models.TextField()
    essential_literature = models.TextField()
    further_reading = models.TextField()
    data = models.DateField()
    publiczne = models.BooleanField()
    edytowalne = models.BooleanField()
    przedmiot = models.OneToOneField('SwierkappPrzedmiot', models.DO_NOTHING)
    assessment_conditions = models.TextField(blank=True, null=True)
    metody_dydaktyczne_stacjonarne = models.TextField(blank=True, null=True)
    metody_dydaktyczne_zdalne = models.TextField(blank=True, null=True)
    skopiuj_efekty_z_eu = models.BooleanField(db_column='skopiuj_efekty_z_EU')  # Field name made lowercase.
    teaching_methods_in_person = models.TextField(blank=True, null=True)
    teaching_methods_online = models.TextField(blank=True, null=True)
    warunki_zaliczenia = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Swierkapp_karta'


class SwierkappKartaMetody(models.Model):
    id = models.BigAutoField(primary_key=True)
    karta = models.ForeignKey(SwierkappKarta, models.DO_NOTHING)
    metodadydaktyczna = models.ForeignKey('SwierkappMetodadydaktyczna', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Swierkapp_karta_metody'
        unique_together = (('karta', 'metodadydaktyczna'),)


class SwierkappKartaMetodyZdalne(models.Model):
    id = models.BigAutoField(primary_key=True)
    karta = models.ForeignKey(SwierkappKarta, models.DO_NOTHING)
    metodadydaktyczna = models.ForeignKey('SwierkappMetodadydaktyczna', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Swierkapp_karta_metody_zdalne'
        unique_together = (('karta', 'metodadydaktyczna'),)


class SwierkappKartaProwadzacy(models.Model):
    id = models.BigAutoField(primary_key=True)
    karta = models.ForeignKey(SwierkappKarta, models.DO_NOTHING)
    user = models.ForeignKey('SwierkappUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Swierkapp_karta_prowadzacy'
        unique_together = (('karta', 'user'),)


class SwierkappKartaPrzedmiotyWprowadzajace(models.Model):
    id = models.BigAutoField(primary_key=True)
    karta = models.ForeignKey(SwierkappKarta, models.DO_NOTHING)
    przedmiot = models.ForeignKey('SwierkappPrzedmiot', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Swierkapp_karta_przedmioty_wprowadzajace'
        unique_together = (('karta', 'przedmiot'),)


class SwierkappKartaZakladaneEfektyKierunkoweKompetencje(models.Model):
    id = models.BigAutoField(primary_key=True)
    karta = models.ForeignKey(SwierkappKarta, models.DO_NOTHING)
    efektkierunkowy = models.ForeignKey(SwierkappEfektkierunkowy, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Swierkapp_karta_zakladane_efekty_kierunkowe_kompetencje'
        unique_together = (('karta', 'efektkierunkowy'),)


class SwierkappKartaZakladaneEfektyKierunkoweUmiejetnosci(models.Model):
    id = models.BigAutoField(primary_key=True)
    karta = models.ForeignKey(SwierkappKarta, models.DO_NOTHING)
    efektkierunkowy = models.ForeignKey(SwierkappEfektkierunkowy, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Swierkapp_karta_zakladane_efekty_kierunkowe_umiejetnosci'
        unique_together = (('karta', 'efektkierunkowy'),)


class SwierkappKartaZakladaneEfektyKierunkoweWiedza(models.Model):
    id = models.BigAutoField(primary_key=True)
    karta = models.ForeignKey(SwierkappKarta, models.DO_NOTHING)
    efektkierunkowy = models.ForeignKey(SwierkappEfektkierunkowy, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Swierkapp_karta_zakladane_efekty_kierunkowe_wiedza'
        unique_together = (('karta', 'efektkierunkowy'),)


class SwierkappKategoriaprzedmiotu(models.Model):
    id = models.BigAutoField(primary_key=True)
    nazwa = models.CharField(unique=True, max_length=256)
    name = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'Swierkapp_kategoriaprzedmiotu'


class SwierkappKierunek(models.Model):
    id = models.BigAutoField(primary_key=True)
    nazwa = models.CharField(unique=True, max_length=128)
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'Swierkapp_kierunek'


class SwierkappMetodadydaktyczna(models.Model):
    id = models.BigAutoField(primary_key=True)
    nazwa = models.TextField()
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'Swierkapp_metodadydaktyczna'


class SwierkappNazwaprzedmiotu(models.Model):
    id = models.BigAutoField(primary_key=True)
    nazwa = models.CharField(unique=True, max_length=256)
    name = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'Swierkapp_nazwaprzedmiotu'


class SwierkappPraca(models.Model):
    id = models.BigAutoField(primary_key=True)
    nr = models.SmallIntegerField()
    praktyczne = models.BooleanField()
    kontaktowe = models.BooleanField()
    opis = models.TextField()
    desc = models.TextField()
    wyliczenie = models.CharField(max_length=32, blank=True, null=True)
    liczba_godzin = models.SmallIntegerField()
    karta = models.ForeignKey(SwierkappKarta, models.DO_NOTHING, blank=True, null=True)
    przedmiot = models.ForeignKey('SwierkappPrzedmiot', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Swierkapp_praca'


class SwierkappPrzedmiot(models.Model):
    id = models.BigAutoField(primary_key=True)
    kod = models.CharField(max_length=16)
    rodzaj = models.CharField(max_length=16)
    sztuczny = models.BooleanField()
    egzamin = models.BooleanField()
    sem = models.SmallIntegerField()
    ects = models.SmallIntegerField()
    liczba_godzin_w = models.SmallIntegerField(db_column='liczba_godzin_W')  # Field name made lowercase.
    liczba_godzin_c = models.SmallIntegerField(db_column='liczba_godzin_C')  # Field name made lowercase.
    liczba_godzin_ps = models.SmallIntegerField(db_column='liczba_godzin_PS')  # Field name made lowercase.
    liczba_godzin_l = models.SmallIntegerField(db_column='liczba_godzin_L')  # Field name made lowercase.
    liczba_godzin_p = models.SmallIntegerField(db_column='liczba_godzin_P')  # Field name made lowercase.
    liczba_godzin_s = models.SmallIntegerField(db_column='liczba_godzin_S')  # Field name made lowercase.
    publiczne = models.BooleanField()
    cykl = models.ForeignKey(SwierkappCykl, models.DO_NOTHING)
    jednostka = models.ForeignKey(SwierkappJednostka, models.DO_NOTHING, blank=True, null=True)
    kategoria = models.ForeignKey(SwierkappKategoriaprzedmiotu, models.DO_NOTHING, blank=True, null=True)
    nazwa = models.ForeignKey(SwierkappNazwaprzedmiotu, models.DO_NOTHING)
    framework_content = models.TextField()
    goals = models.TextField()
    info_dzialalnosc_naukowa = models.BooleanField()
    info_umiejetnosci_praktyczne = models.BooleanField()
    info_zrownowazony_rozwoj = models.BooleanField()
    tresci_ramowe = models.TextField()
    zalozenia = models.TextField()
    edytowalne = models.BooleanField()
    grupa_obieralna = models.ForeignKey(SwierkappNazwaprzedmiotu, models.DO_NOTHING, related_name='swierkappprzedmiot_grupa_obieralna_set', blank=True, null=True)
    data = models.DateField()

    class Meta:
        managed = False
        db_table = 'Swierkapp_przedmiot'


class SwierkappPrzedmiotEfektyKierunkowe(models.Model):
    id = models.BigAutoField(primary_key=True)
    przedmiot = models.ForeignKey(SwierkappPrzedmiot, models.DO_NOTHING)
    efektkierunkowy = models.ForeignKey(SwierkappEfektkierunkowy, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Swierkapp_przedmiot_efekty_kierunkowe'
        unique_together = (('przedmiot', 'efektkierunkowy'),)


class SwierkappPrzedmiotKoordynatorzy(models.Model):
    id = models.BigAutoField(primary_key=True)
    przedmiot = models.ForeignKey(SwierkappPrzedmiot, models.DO_NOTHING)
    user = models.ForeignKey('SwierkappUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Swierkapp_przedmiot_koordynatorzy'
        unique_together = (('przedmiot', 'user'),)


class SwierkappPrzedmiotOpiekunowie(models.Model):
    id = models.BigAutoField(primary_key=True)
    przedmiot = models.ForeignKey(SwierkappPrzedmiot, models.DO_NOTHING)
    user = models.ForeignKey('SwierkappUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Swierkapp_przedmiot_opiekunowie'
        unique_together = (('przedmiot', 'user'),)


class SwierkappPrzedmiotPulaPrzedmiotow(models.Model):
    id = models.BigAutoField(primary_key=True)
    from_przedmiot = models.ForeignKey(SwierkappPrzedmiot, models.DO_NOTHING)
    to_przedmiot = models.ForeignKey(SwierkappPrzedmiot, models.DO_NOTHING, related_name='swierkappprzedmiotpulaprzedmiotow_to_przedmiot_set')

    class Meta:
        managed = False
        db_table = 'Swierkapp_przedmiot_pula_przedmiotow'
        unique_together = (('from_przedmiot', 'to_przedmiot'),)


class SwierkappSemestr(models.Model):
    id = models.BigAutoField(primary_key=True)
    rok_akademicki = models.IntegerField()
    zimowy_letni = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'Swierkapp_semestr'


class SwierkappSpecjalnosc(models.Model):
    id = models.BigAutoField(primary_key=True)
    nazwa = models.CharField(unique=True, max_length=64)
    name = models.CharField(max_length=64)
    kierunek = models.ForeignKey(SwierkappKierunek, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Swierkapp_specjalnosc'


class SwierkappStudia(models.Model):
    id = models.BigAutoField(primary_key=True)
    liczba_semestrow = models.SmallIntegerField()
    opis = models.CharField(max_length=64)
    desc = models.CharField(max_length=64)
    stopien = models.CharField(max_length=8)
    forma = models.CharField(max_length=16, blank=True, null=True)
    profil = models.CharField(max_length=32, blank=True, null=True)
    kierunek = models.ForeignKey(SwierkappKierunek, models.DO_NOTHING)
    specjalnosc = models.ForeignKey(SwierkappSpecjalnosc, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Swierkapp_studia'


class SwierkappUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    is_teacher = models.BooleanField()
    is_administrator_siatek = models.BooleanField()
    tytul = models.CharField(max_length=64, blank=True, null=True)
    stanowisko = models.CharField(max_length=64, blank=True, null=True)
    firma = models.CharField(max_length=128, blank=True, null=True)
    token = models.CharField(max_length=64, blank=True, null=True)
    katedra = models.ForeignKey(SwierkappJednostka, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Swierkapp_user'


class SwierkappUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(SwierkappUser, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Swierkapp_user_groups'
        unique_together = (('user', 'group'),)


class SwierkappUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(SwierkappUser, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Swierkapp_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuditlogLogentry(models.Model):
    object_pk = models.CharField(max_length=255)
    object_id = models.BigIntegerField(blank=True, null=True)
    object_repr = models.TextField()
    action = models.SmallIntegerField()
    changes = models.TextField()
    timestamp = models.DateTimeField()
    actor = models.ForeignKey(SwierkappUser, models.DO_NOTHING, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    remote_addr = models.GenericIPAddressField(blank=True, null=True)
    additional_data = models.JSONField(blank=True, null=True)
    serialized_data = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auditlog_logentry'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(SwierkappUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
