__author__ = 'tomasz'

from SymulacjaSwiata import Roslina


class Guarana(Roslina.Roslina):
    def __init__(self):
        super().__init__()
        self.nazwa = "Guarana"
        self.sila = 0
        self.znak = 'G'
        self.kolor = "magenta"

    def kolizjaobrona(self, a):
        a.zwiekszsile()
        if self.sila > a.zwrocsile():
            return True
        return False
        pass

    pass
