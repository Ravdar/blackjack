class Gracz:
    """Klasa gracza"""

    def __init__(self, imie, bankroll=500, karty=[]):
        """Określenie atrybutów początkowych klasy Gracz"""

        self.imie = imie
        self.bankroll = bankroll
        self.karty = karty

    def bankrut(self):
        """Operacje w przypadku bankructwa gracza"""

        if self.bankroll == 0:
            print(f"BANKRUT! {self.imie} ma 0 $ na koncie. Koniec gry.")
            return True
        else:
            return False

    def punkty_gracza(self):
        """Określenie aktualnej ręki gracza"""
        suma = 0

        for karta in self.karty:
            suma += karta.ranga

        return suma

    def pokaz_karty(self):
        """Zwraca listę kart gracza"""

        lista_kart = []
        for i in self.karty:
            lista_kart.append(i.pokaz_karte())
        return lista_kart
