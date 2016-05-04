__author__ = 'tomasz'

from SymulacjaSwiata import Zwierze
import random


class Antylopa(Zwierze.Zwierze):
    def __init__(self):
        super().__init__()
        self.nazwa = "Antylopa"
        self.sila = 4
        self.inicjatywa = 4
        self.znak = 'A'
        self.kolor = "orange"

    pass

    def akcja(self):
        self.ruszsie()
        self.ruszsie()

    pass

    def kolizjaobrona(self, a):
        if random.randrange(0, 3) != 0:
            self.ruszsie()
            return True
        if self.sila > a.zwrocsile():
            return True
        return False

    pass

    def kolizjaatak(self, a):
        if random.randrange(0, 3) != 0:
            self.ruszsie()
            return True
        if self.sila >= a.zwrocsile():
            return True
        return False

    pass
    pass
