__author__ = 'tomasz'

import random
import SymulacjaSwiata
import linecache


class Swiat:
    KolejkaOroganizmow = []
    raporty = []
    organizmy = []
    comp = []
    usuniecie = []
    ruch_czlowieka = 0
    dodawany = 0
    dodawaniex = 0
    dodawaniey = 0

    def dodaj_nowy(self):
        if self.dodawany == 0:
            self.organizmy.append(SymulacjaSwiata.Wilk.Wilk())
        elif self.dodawany == 1:
            self.organizmy.append(SymulacjaSwiata.Owca.Owca())
        elif self.dodawany == 6:
            self.organizmy.append(SymulacjaSwiata.Trawa.Trawa())
        elif self.dodawany == 3:
            self.organizmy.append(SymulacjaSwiata.Guarana.Guarana())
        elif self.dodawany == 5:
            self.organizmy.append(SymulacjaSwiata.Mlecz.Mlecz())
        elif self.dodawany == 7:
            self.organizmy.append(SymulacjaSwiata.WilczeJagody.WilczeJagody())
        elif self.dodawany == 4:
            self.organizmy.append(SymulacjaSwiata.Lis.Lis())
        elif self.dodawany == 8:
            self.organizmy.append(SymulacjaSwiata.Zolw.Zolw())
        elif self.dodawany == 2:
            self.organizmy.append(SymulacjaSwiata.Antylopa.Antylopa())
        self.organizmy[len(self.organizmy) - 1].ustawpolozenie(self.dodawaniex, self.dodawaniey)
        pass

    def wykonajTure(self, ruch_czlowieka2):
        assert isinstance(ruch_czlowieka2, int)
        self.ruch_czlowieka = ruch_czlowieka2
        self.KolejkaOroganizmow = []
        self.raporty = []
        for (i, elem) in enumerate(self.organizmy):
            self.KolejkaOroganizmow.append(i)
        for (i, elem) in enumerate(self.KolejkaOroganizmow):
            for (j, elem2) in enumerate(self.KolejkaOroganizmow):
                if self.porownaj(self.organizmy[elem].zwrocinicjatywe(), self.organizmy[elem2].zwrocinicjatywe(),
                                 self.organizmy[elem].zwrocwiek(), self.organizmy[elem2].zwrocwiek()):
                    self.KolejkaOroganizmow[i], self.KolejkaOroganizmow[j] = self.KolejkaOroganizmow[j], \
                                                                             self.KolejkaOroganizmow[i]
        for (i, elem) in enumerate(self.KolejkaOroganizmow):
            if not self.organizmy[self.KolejkaOroganizmow[i]].czyzyje():
                continue
            self.organizmy[self.KolejkaOroganizmow[i]].skopiuj_wszystko(self.organizmy, self.usuniecie,
                                                                        self.ruch_czlowieka, self.raporty)
            self.organizmy[self.KolejkaOroganizmow[i]].akcja()
            self.organizmy[self.KolejkaOroganizmow[i]].ile_raportow(self.organizmy, self.usuniecie, self.raporty)
            self.organizmy[self.KolejkaOroganizmow[i]].dodajlat()
            if self.organizmy[self.KolejkaOroganizmow[i]].czymnozyc():
                if self.organizmy[self.KolejkaOroganizmow[i]].zwrocnazwe() == "Wilk":
                    self.organizmy.append(SymulacjaSwiata.Wilk.Wilk())
                elif self.organizmy[self.KolejkaOroganizmow[i]].zwrocnazwe() == "Owca":
                    self.organizmy.append(SymulacjaSwiata.Owca.Owca())
                elif self.organizmy[self.KolejkaOroganizmow[i]].zwrocnazwe() == "Trawa":
                    self.organizmy.append(SymulacjaSwiata.Trawa.Trawa())
                elif self.organizmy[self.KolejkaOroganizmow[i]].zwrocnazwe() == "Guarana":
                    self.organizmy.append(SymulacjaSwiata.Guarana.Guarana())
                elif self.organizmy[self.KolejkaOroganizmow[i]].zwrocnazwe() == "Mlecz":
                    self.organizmy.append(SymulacjaSwiata.Mlecz.Mlecz())
                elif self.organizmy[self.KolejkaOroganizmow[i]].zwrocnazwe() == "WilczeJagody":
                    self.organizmy.append(SymulacjaSwiata.WilczeJagody.WilczeJagody())
                elif self.organizmy[self.KolejkaOroganizmow[i]].zwrocnazwe() == "Lis":
                    self.organizmy.append(SymulacjaSwiata.Lis.Lis())
                elif self.organizmy[self.KolejkaOroganizmow[i]].zwrocnazwe() == "Zolw":
                    self.organizmy.append(SymulacjaSwiata.Zolw.Zolw())
                elif self.organizmy[self.KolejkaOroganizmow[i]].zwrocnazwe() == "Antylopa":
                    self.organizmy.append(SymulacjaSwiata.Antylopa.Antylopa())
                czyraport = True
                if (random.randrange(0, 5) != 0) and (
                            self.organizmy[self.KolejkaOroganizmow[i]].zwrocx() != 19) and self.czywolne(
                            self.organizmy[self.KolejkaOroganizmow[i]].zwrocx() + 1,
                    self.organizmy[self.KolejkaOroganizmow[i]].zwrocy()):
                    self.organizmy[len(self.organizmy) - 1].ustawpolozenie(
                        self.organizmy[self.KolejkaOroganizmow[i]].zwrocx() + 1,
                        self.organizmy[self.KolejkaOroganizmow[i]].zwrocy())
                elif random.randrange(0, 5) != 0 and self.organizmy[
                    self.KolejkaOroganizmow[i]].zwrocx() != 0 and self.czywolne(
                            self.organizmy[self.KolejkaOroganizmow[i]].zwrocx() - 1,
                    self.organizmy[self.KolejkaOroganizmow[i]].zwrocy()):
                    self.organizmy[len(self.organizmy) - 1].ustawpolozenie(
                        self.organizmy[self.KolejkaOroganizmow[i]].zwrocx() - 1,
                        self.organizmy[self.KolejkaOroganizmow[i]].zwrocy())
                elif random.randrange(0, 5) != 0 and self.organizmy[
                    self.KolejkaOroganizmow[i]].zwrocy() != 19 and self.czywolne(
                    self.organizmy[self.KolejkaOroganizmow[i]].zwrocx(),
                            self.organizmy[self.KolejkaOroganizmow[i]].zwrocy() + 1):
                    self.organizmy[len(self.organizmy) - 1].ustawpolozenie(
                        self.organizmy[self.KolejkaOroganizmow[i]].zwrocx(),
                        self.organizmy[self.KolejkaOroganizmow[i]].zwrocy() + 1)
                elif random.randrange(0, 5) != 0 and self.organizmy[
                    self.KolejkaOroganizmow[i]].zwrocy() != 0 and self.czywolne(
                    self.organizmy[self.KolejkaOroganizmow[i]].zwrocx(),
                            self.organizmy[self.KolejkaOroganizmow[i]].zwrocy() - 1):
                    self.organizmy[len(self.organizmy) - 1].ustawpolozenie(
                        self.organizmy[self.KolejkaOroganizmow[i]].zwrocx(),
                        self.organizmy[self.KolejkaOroganizmow[i]].zwrocy() - 1)
                else:
                    czyraport = False
                    self.organizmy.remove(self.organizmy[len(self.organizmy) - 1])
                if czyraport:
                    self.raporty.append("Pojawia sie " + str(
                        self.organizmy[self.KolejkaOroganizmow[i]].zwrocnazwe()) + " w polu " + str(
                        self.organizmy[len(self.organizmy) - 1].zwrocx()) + " " + str(
                        self.organizmy[len(self.organizmy) - 1].zwrocy()))
                self.organizmy[self.KolejkaOroganizmow[i]].niemnoz()
            pom = self.czykolizja(self.KolejkaOroganizmow[i])
            if pom != -1:
                if self.organizmy[self.KolejkaOroganizmow[i]].zwrocnazwe() == self.organizmy[pom].zwrocnazwe():
                    if not self.organizmy[self.KolejkaOroganizmow[i]].czymnozyc() and not self.organizmy[
                        pom].czymnozyc():
                        self.organizmy[self.KolejkaOroganizmow[i]].mnoz()
                elif self.organizmy[pom].czyzyje() and self.organizmy[self.KolejkaOroganizmow[i]].czyzyje():
                    pom2 = self.kolizja(self.organizmy[self.KolejkaOroganizmow[i]], self.organizmy[pom])
                    if pom2 == 1:
                        self.raporty.append(
                            "zginal " + str(self.organizmy[self.KolejkaOroganizmow[i]].zwrocnazwe()) + " przez " + str(
                                self.organizmy[pom].zwrocnazwe()) + " w polu " + str(
                                self.organizmy[pom].zwrocx()) + " " + str(self.organizmy[pom].zwrocy()))
                        self.usuniecie.append(self.KolejkaOroganizmow[i])
                        self.organizmy[self.KolejkaOroganizmow[i]].zemzyj()
                    if pom2 == -1:
                        self.raporty.append("zginal " + str(self.organizmy[pom].zwrocnazwe()) + " przez " + str(
                            self.organizmy[self.KolejkaOroganizmow[i]].zwrocnazwe()) + " w polu " + str(
                            self.organizmy[pom].zwrocx()) + " " + str(self.organizmy[pom].zwrocy()))
                        self.usuniecie.append(pom)
                        self.organizmy[pom].zemzyj()
        self.usuniecie.sort()
        while len(self.usuniecie) > 0:
            self.organizmy.remove(self.organizmy[self.usuniecie.pop()])
        pass

    def porownaj(self, in1, in2, wiek1, wiek2):
        if in1 == in2:
            return wiek1 > wiek2
        return in1 > in2
        pass

    def czykolizja(self, n) -> int:
        for (i, elem) in enumerate(self.organizmy):
            if (self.organizmy[i].zwrocx() == self.organizmy[n].zwrocx() and self.organizmy[i].zwrocy() ==
                self.organizmy[n].zwrocy() and i != n):
                return i
        return -1
        pass

    def czywolne(self, x, y):
        for (i, elem) in enumerate(self.organizmy):
            if elem.polozeniex == x and elem.polozeniey == y:
                return False
        return True
        pass

    def kolizja(self, a, b):
        wynik2 = 0
        wynik1 = 0
        if a.kolizjaatak(b):
            wynik1 = 1
        else:
            wynik1 = 0
        if b.kolizjaobrona(a):
            wynik2 = 1
        else:
            wynik2 = 0
        pom = wynik1 * 2 + wynik2
        if pom == 1:
            return 1
        if pom == 2:
            return -1
        return 0
        pass

    def naPozycji(self, x, y):
        for (i, elem) in enumerate(self.organizmy):
            if self.organizmy[i].zwrocx() == x and self.organizmy[i].zwrocy() == y:
                return self.organizmy[i]
        return None
        pass

    def transfer(self, x, y, s):
        self.organizmy.append(s.naPozycji(x, y))
        pass

    def stangry(self):
        if len(self.organizmy) == 1 and self.organizmy[0].zwrocnazwe() == "Czlowiek":
            return 1
        for (i, elem) in enumerate(self.organizmy):
            if self.organizmy[i].zwrocnazwe() == "Czlowiek":
                return 0
        return 2
        pass

    def __init__(self):
        self.dodawany = 0
        self.dodac = False
        self.organizmy = []
        self.organizmy.append(SymulacjaSwiata.Czlowiek.Czlowiek())
        i = 0
        while i < 2:
            self.organizmy.append(SymulacjaSwiata.Lis.Lis())
            self.organizmy.append(SymulacjaSwiata.Owca.Owca())
            self.organizmy.append(SymulacjaSwiata.Wilk.Wilk())
            self.organizmy.append(SymulacjaSwiata.Zolw.Zolw())
            self.organizmy.append(SymulacjaSwiata.Antylopa.Antylopa())
            self.organizmy.append(SymulacjaSwiata.Guarana.Guarana())
            self.organizmy.append(SymulacjaSwiata.Trawa.Trawa())
            self.organizmy.append(SymulacjaSwiata.Mlecz.Mlecz())
            self.organizmy.append(SymulacjaSwiata.WilczeJagody.WilczeJagody())
            i += 1
        for (i, elem) in enumerate(self.organizmy):
            x = 0
            y = 0
            while True:
                x = random.randrange(0, 20)
                y = random.randrange(0, 20)
                if not self.czywolne(x, y):
                    continue
                break
            self.organizmy[i].ustawpolozenie(x, y)
        pass

    def zapiszDoPliku(self):
        zapis = []
        zapis.append(str(len(self.organizmy)) + "\n")
        for (i, elem) in enumerate(self.organizmy):
            zapis.append(str(self.organizmy[i].zwrocznak()) + " " + str(self.organizmy[i].zwrocwiek()) + " " + str(
                self.organizmy[
                    i].zwrocsile()) + " " + str(self.organizmy[i].zwrocinicjatywe()) + " " + str(
                self.organizmy[i].zwrocx()) + " " +
                         str(self.organizmy[i].zwrocy()) + "\n")
        plik = open('Zapis.txt', 'w')
        plik.writelines(zapis)
        plik.close()
        pass

    def wczytajzPliku(self):
        self.organizmy = []
        self.raporty = []
        org = []
        n = 1
        liczba = int('0' + linecache.getline('Zapis.txt', 1))
        while n <= liczba:
            odczyt = linecache.getline('Zapis.txt', n + 1)
            org = odczyt.split(' ')
            typ = org[0]
            wiek = int(org[1])
            sila = int(org[2])
            inicjatywa = int(org[3])
            pozX = int(org[4])
            pozY = int(org[5])
            if typ == 'W':
                self.organizmy.append(SymulacjaSwiata.Wilk.Wilk())
            elif typ == 'O':
                self.organizmy.append(SymulacjaSwiata.Owca.Owca())
            elif typ == 'T':
                self.organizmy.append(SymulacjaSwiata.Trawa.Trawa())
            elif typ == 'G':
                self.organizmy.append(SymulacjaSwiata.Guarana.Guarana())
            elif typ == 'M':
                self.organizmy.append(SymulacjaSwiata.Mlecz.Mlecz())
            elif typ == 'J':
                self.organizmy.append(SymulacjaSwiata.WilczeJagody.WilczeJagody())
            elif typ == 'L':
                self.organizmy.append(SymulacjaSwiata.Lis.Lis())
            elif typ == 'Z':
                self.organizmy.append(SymulacjaSwiata.Zolw.Zolw())
            elif typ == 'A':
                self.organizmy.append(SymulacjaSwiata.Antylopa.Antylopa())
            elif typ == 'C':
                self.organizmy.append(SymulacjaSwiata.Czlowiek.Czlowiek())
            self.organizmy[len(self.organizmy) - 1].ustaw(wiek, sila, inicjatywa)
            self.organizmy[len(self.organizmy) - 1].polozenie(pozX, pozY)
            n += 1
        pass

    pass
