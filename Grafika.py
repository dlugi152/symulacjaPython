__author__ = 'tomasz'

from tkinter import *
from tkinter import ttk


class Grafika:
    Szerokosc_Okienka = 900
    Wysokosc_Okienka = 700
    refSwiat = None
    nazwa_planszy = None

    def __init__(self, refS):
        self.refSwiat = refS
        Grafika.initUi(self)
        pass

    def weryfikacja(self, pomx, pomy):
        if 0 <= pomx < 20 and 0 <= pomy < 20 and self.refSwiat.czywolne(pomx, pomy):
            self.refSwiat.dodawaniex = pomx
            self.refSwiat.dodawaniey = pomy
            self.refSwiat.dodaj_nowy()
        pass

    def ustaw(self, zwierze):
        self.refSwiat.dodawany = zwierze
        pass

    def aktualizuj(self, basic):
        czysc = Canvas(basic, width=600, height=400)
        czysc.grid(row=1, column=9, columnspan=4, rowspan=3)
        czysc.create_rectangle(0, 0, 300, 600, fill="snow")
        w = Canvas(basic, width=600, height=600)
        self.nazwa_planszy = w._name
        w.grid(row=0, column=0, rowspan=2, columnspan=9)
        for (i, elem) in enumerate(self.refSwiat.raporty):
            napis = Label(basic, text=self.refSwiat.raporty[i], background='snow')
            napis.place(x=605, y=310 + i * 20)
        for x in range(20):
            for y in range(20):
                w.create_rectangle(x * 30, y * 30, (x + 1) * 30, (y + 1) * 30, fill="gainsboro")
        for (i, elem) in enumerate(self.refSwiat.organizmy):
            w.create_rectangle(self.refSwiat.organizmy[i].zwrocx() * 30,
                               self.refSwiat.organizmy[i].zwrocy() * 30, (self.refSwiat.organizmy[i].zwrocx() + 1) * 30,
                               (self.refSwiat.organizmy[i].zwrocy() + 1) * 30,
                               fill=self.refSwiat.organizmy[i].getKolor())
        pass

    def czytaj(self, basic):
        self.refSwiat.wczytajzPliku()
        self.aktualizuj(basic)
        pass

    def initUi(self):
        root = Tk()
        root.geometry("%dx%d+0+0" % (self.Szerokosc_Okienka, self.Wysokosc_Okienka))
        root.title("Tomasz Dlugokinski 149174")
        basic = ttk.Frame(root)
        basic.grid(sticky=(N, W, E, S))

        self.aktualizuj(basic)

        w2 = Canvas(basic, width=400, height=300)
        for y in range(10):  # to miało tworzyć legendę co kolory oznaczają
            NazwaZwierzecia = "0"
            kolor = "black"
            if y == 0:
                NazwaZwierzecia = "Wilk"
                kolor = "black"
            elif y == 1:
                NazwaZwierzecia = "Owca"
                kolor = "white"
            elif y == 2:
                NazwaZwierzecia = "Antylopa"
                kolor = "orange"
            elif y == 3:
                NazwaZwierzecia = "Guarana"
                kolor = "magenta"
            elif y == 4:
                NazwaZwierzecia = "Lis"
                kolor = "cyan"
            elif y == 5:
                NazwaZwierzecia = "Mlecz"
                kolor = "yellow"
            elif y == 6:
                NazwaZwierzecia = "Trawa"
                kolor = "green"
            elif y == 7:
                NazwaZwierzecia = "WilczeJagody"
                kolor = "pink"
            elif y == 8:
                NazwaZwierzecia = "Zolw"
                kolor = "light gray"
            elif y == 9:
                NazwaZwierzecia = "Czlowiek"
                kolor = "blue"
            napis = Label(basic, text=NazwaZwierzecia)
            napis.place(x=640, y=y * 30, width=75, height=30)
            w2.grid(row=0, column=9, sticky=W)
            w2.create_rectangle(0, y * 30, 30, (y + 1) * 30, fill=kolor)

        Button(basic, text="Wilk", fg="red", command=lambda: self.ustaw(0)).grid(row=2, column=0)
        Button(basic, text="Owca", fg="red", command=lambda: self.ustaw(1)).grid(row=2, column=1)
        Button(basic, text="Antylopa", fg="red", command=lambda: self.ustaw(2)).grid(row=2, column=2)
        Button(basic, text="Guarana", fg="red", command=lambda: self.ustaw(3)).grid(row=2, column=3)
        Button(basic, text="Lis", fg="red", command=lambda: self.ustaw(4)).grid(row=2, column=4)
        Button(basic, text="Mlecz", fg="red", command=lambda: self.ustaw(5)).grid(row=2, column=5)
        Button(basic, text="Trawa", fg="red", command=lambda: self.ustaw(6)).grid(row=2, column=6)
        Button(basic, text="WilczeJagody", fg="red", command=lambda: self.ustaw(7)).grid(row=2, column=7)
        Button(basic, text="Zolw", fg="red", command=lambda: self.ustaw(8)).grid(row=2, column=8)
        Button(basic, text="Wyjscie", fg="blue", command=basic.quit).grid(row=3, column=0)
        Button(basic, text="Zapisz", fg="blue", command=lambda: self.refSwiat.zapiszDoPliku()).grid(row=3, column=1)
        Button(basic, text="Wczytaj", fg="blue", command=lambda: self.czytaj(basic)).grid(row=3, column=2)

        def handleKeypress(event):
            if event.keysym == "Left":
                self.refSwiat.wykonajTure(1)
            elif event.keysym == "Right":
                self.refSwiat.wykonajTure(0)
            elif event.keysym == "Up":
                self.refSwiat.wykonajTure(3)
            elif event.keysym == "Down":
                self.refSwiat.wykonajTure(2)
            elif event.keysym == "space":
                self.refSwiat.wykonajTure(-1)
            self.aktualizuj(basic)
            pass

        def callback(event):
            if event.widget._name == self.nazwa_planszy:
                self.weryfikacja(int(event.x / 30), int(event.y / 30))
                self.aktualizuj(basic)
            pass

        root.bind_all("<Key>", handleKeypress)
        root.bind("<Button-1>", callback)
        root.mainloop()
        pass

    pass