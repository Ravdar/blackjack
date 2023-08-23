class Karta:
    """Klasa karty"""

    def __init__(self, kolor, figura, ranga):
        """Określenie atrybutów początkowych klasy Karta"""

        self.kolor = kolor
        self.figura = figura
        self.ranga = ranga

    def pokaz_karte(self):
        """Zwraca figurę i kolor karty"""

        return f"{self.figura} {self.kolor}"

