__author__ = 'tomasz'

import random
from SymulacjaSwiata import Organizm


class Zwierze(Organizm.Organizm):
    def ruszsie(self):
        petla = 1
        while petla == 1:
            n = random.randrange(0, 5)
            if (n == 0) and (self.polozeniex != 19):
                self.polozenie(self.polozeniex + 1, self.polozeniey)
                break
            if (n == 1) and (self.polozeniex != 0):
                self.polozenie(self.polozeniex - 1, self.polozeniey)
                break
            if (n == 2) and (self.polozeniey != 19):
                self.polozenie(self.polozeniex, self.polozeniey + 1)
                break
            if (n == 3) and (self.polozeniey != 0):
                self.polozenie(self.polozeniex, self.polozeniey - 1)
                break
        pass

    def akcja(self):
        self.ruszsie()

    def mnoz(self):
        self.potomek = 1
        pass

    def kolizjaatak(self, a):
        if self.sila >= a.zwrocsile():
            return True
        return False
        pass

    def kolizjaobrona(self, a):
        if self.sila > a.zwrocsile():
            return True
        return False
        pass

    def __init__(self):
        super().__init__()
        self.wiek = 0
        self.potomek = 0

    pass
