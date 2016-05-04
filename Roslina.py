__author__ = 'tomasz'

from SymulacjaSwiata import Organizm
import random


class Roslina(Organizm.Organizm):
    def akcja(self):
        self.mnoz()
        pass

    def __init__(self):
        super().__init__()
        self.inicjatywa = self.wiek = 0

    def kolizjaobrona(self, a):
        if self.sila > a.zwrocsile():
            return True
        return False
        pass

    def kolizjaatak(self, a):
        if self.sila >= a.zwrocsile():
            return True
        return False
        pass

    def mnoz(self):
        if random.randrange(0, 11) == 0:
            self.potomek = 1
        pass

    pass
