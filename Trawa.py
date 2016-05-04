__author__ = 'tomasz'

from SymulacjaSwiata import Roslina


class Trawa(Roslina.Roslina):
    def __init__(self):
        super().__init__()
        self.nazwa = "Trawa"
        self.sila = 0
        self.znak = 'T'
        self.kolor = "green"

    pass
