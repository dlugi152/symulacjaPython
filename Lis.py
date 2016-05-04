__author__ = 'tomasz'

from SymulacjaSwiata import Zwierze
import random


class Lis(Zwierze.Zwierze):
    def __init__(self):
        super().__init__()
        self.nazwa = "Lis"
        self.sila = 3
        self.inicjatywa = 7
        self.znak = 'L'
        self.kolor = "cyan"

    def czy_mozna_isc(self, x, y):
        for (i, elem) in enumerate(self.organizmy):
            if (self.organizmy[i].zwrocx() == x and self.organizmy[i].zwrocy() == y and self.organizmy[
                i].zwrocsile() > self.sila):
                return True
        return False
        pass

    def ruszsie(self):
        petla = 1
        while petla == 1:
            n = random.randrange(0, 5)
            if n == 0 and self.polozeniex != 19 and not self.czy_mozna_isc(self.polozeniex + 1, self.polozeniey):
                petla = 0
                self.polozenie(self.polozeniex + 1, self.polozeniey)
            if n == 0 and self.polozeniex != 0 and not self.czy_mozna_isc(self.polozeniex - 1, self.polozeniey):
                petla = 0
                self.polozenie(self.polozeniex - 1, self.polozeniey)
            if n == 0 and self.polozeniey != 19 and not self.czy_mozna_isc(self.polozeniex, self.polozeniey + 1):
                petla = 0
                self.polozenie(self.polozeniex, self.polozeniey + 1)
            if n == 0 and self.polozeniey != 19 and not self.czy_mozna_isc(self.polozeniex, self.polozeniey - 1):
                petla = 0
                self.polozenie(self.polozeniex, self.polozeniey - 1)
        pass

    def akcja(self):
        self.ruszsie()
        pass

    pass
