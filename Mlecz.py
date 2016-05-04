__author__ = 'tomasz'

from SymulacjaSwiata import Roslina


class Mlecz(Roslina.Roslina):
    def __init__(self):
        super().__init__()
        self.nazwa = "Mlecz"
        self.sila = 0
        self.znak = 'M'
        self.kolor = "Yellow"

    def akcja(self):
        self.mnoz()
        self.mnoz()
        self.mnoz()
        pass

    pass
