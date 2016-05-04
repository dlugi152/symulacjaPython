__author__ = 'tomasz'

from SymulacjaSwiata import Zwierze
import math


class Czlowiek(Zwierze.Zwierze):
    # kolor=Color.ORANGE;
    calopalenie = False
    cooldown = 5

    def __init__(self):
        super().__init__()
        self.nazwa = "Czlowiek"
        self.sila = self.cooldown = 5
        self.inicjatywa = 4
        self.znak = 'C'
        self.calopalenie = False
        self.kolor = "blue"

    def pal_wszystko(self):
        for (i, elem) in enumerate(self.organizmy):
            if (math.fabs(self.organizmy[i].zwrocx() - self.polozeniex) <= 1 and math.fabs(
                        self.organizmy[i].zwrocy() - self.polozeniey) <= 1 and self.organizmy[
                i].zwrocnazwe() != self.nazwa):
                self.usuniecie.append(i)
                self.organizmy[i].zemzyj()
                self.raporty.append(
                    "Czlowiek \"calopali\" " + str(self.organizmy[i].zwrocnazwe()) + " w polu " +
                    str(self.organizmy[i].zwrocx()) + " " + str(self.organizmy[i].zwrocy()))
        pass

    def ruszsie(self):
        if self.ruch_czlowieka == 0 and self.polozeniex != 19:
            self.polozenie(self.polozeniex + 1, self.polozeniey)
        if self.ruch_czlowieka == 1 and self.polozeniex != 0:
            self.polozenie(self.polozeniex - 1, self.polozeniey)
        if self.ruch_czlowieka == 2 and self.polozeniey != 19:
            self.polozenie(self.polozeniex, self.polozeniey + 1)
        if self.ruch_czlowieka == 3 and self.polozeniey != 0:
            self.polozenie(self.polozeniex, self.polozeniey - 1)
        if self.ruch_czlowieka == -1 and self.cooldown == 5:
            self.calopalenie = True
        pass

    def akcja(self):
        self.ruszsie()
        if self.cooldown == 0:
            self.calopalenie = False
        if self.calopalenie:
            self.cooldown -= 1
        elif self.cooldown != 5:
            self.cooldown += 1
        if self.calopalenie:
            self.pal_wszystko()
        pass

    pass
