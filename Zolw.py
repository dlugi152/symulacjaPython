__author__ = 'tomasz'

from SymulacjaSwiata import Zwierze
import random


class Zolw(Zwierze.Zwierze):
    def __init__(self):
        super().__init__()
        self.nazwa = "Zolw"
        self.sila = 2
        self.inicjatywa = 1
        self.znak = 'Z'
        self.kolor = "light gray"

    def akcja(self):
        if random.randrange(0, 5) == 3:
            self.ruszsie()
        pass

    def kolizjaobrona(self, a):
        if a.zwrocsile() < 5:
            a.akcja()
            return True
        return False
        pass

    pass
