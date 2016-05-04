__author__ = 'tomasz'

from SymulacjaSwiata import Zwierze


class Wilk(Zwierze.Zwierze):
    def __init__(self):
        super().__init__()
        self.nazwa = "Wilk"
        self.sila = 9
        self.inicjatywa = 4
        self.znak = 'W'
        self.kolor = "black"

    pass
