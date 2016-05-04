__author__ = 'tomasz'

from SymulacjaSwiata import Zwierze


class Owca(Zwierze.Zwierze):
    def __init__(self):
        super().__init__()
        self.nazwa = "Owca"
        self.sila = 4
        self.inicjatywa = 4
        self.znak = 'O'
        self.kolor = "white"

    pass
