__author__ = 'tomasz'


class Organizm:
    sila = 0
    inicjatywa = 0
    wiek = 0
    polozeniex = 0
    polozeniey = 0
    potomek = 0
    znak = 'a'
    martwy = False
    nazwa = ""
    ruch_czlowieka = 0
    swiat = None
    organizmy = []
    usuniecie = []
    raporty = []
    raport = 0
    kolor = None

    def __init__(self):
        self.martwy = False
        self.potomek = 0
        self.wiek = 0
        pass

    def dodajlat(self):
        self.wiek += 1
        pass

    def getKolor(self):
        return self.kolor
        pass

    def zwrocinicjatywe(self):
        return self.inicjatywa
        pass

    def skopiuj_wszystko(self, organizmy2, usuniecie2, ruch_czlowieka2, raporty2):
        self.organizmy = organizmy2
        self.ruch_czlowieka = ruch_czlowieka2
        self.usuniecie = usuniecie2
        self.raporty = raporty2
        pass

    def ile_raportow(self, organizmy2, usuniecie2, raporty2):
        usuniecie2 = self.usuniecie
        organizmy2 = self.organizmy
        raporty2 = self.raporty
        pass

    def polozenie(self, x, y):
        self.polozeniex = x
        self.polozeniey = y
        pass

    def zwrocwiek(self):
        return self.wiek
        pass

    def zwrocx(self):
        return self.polozeniex
        pass

    def zwrocy(self):
        return self.polozeniey
        pass

    def zwrocsile(self):
        return self.sila
        pass

    def zwrocnazwe(self):
        return self.nazwa
        pass

    def zwrocznak(self):
        return self.znak
        pass

    def ustaw(self, wiek2, sila2, inicjatywa2):
        self.wiek = wiek2
        self.sila = sila2
        self.inicjatywa = inicjatywa2
        pass

    def ustawpolozenie(self, x, y):
        self.polozeniex = x
        self.polozeniey = y
        pass

    def czymnozyc(self):
        return self.potomek != 0
        pass

    def niemnoz(self):
        self.potomek = 0
        pass

    def zemzyj(self):
        self.martwy = True
        pass

    def zwiekszsile(self):
        self.sila += 3
        pass

    def czyzyje(self):
        return not self.martwy
        pass

    pass
