__author__ = 'tomasz'

from SymulacjaSwiata import Roslina


class WilczeJagody(Roslina.Roslina):
    def __init__(self):
        super().__init__()
        self.nazwa = "WilczeJagody"
        self.sila = 99
        self.znak = 'J'
        self.kolor = "pink"

    pass
