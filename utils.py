import random
from karta import Karta


def utworz_talie():
    """Tworzy talię 54 kart"""

    kolory = ["Trefl", "Karo", "Kier", "Pik"]
    figury = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "Jopek": 10,
        "Dama": 10,
        "Król": 10,
        "As": 11,
    }
    talia_lista = []

    for kolor in kolory:
        for figura in figury:
            karta = Karta(kolor, figura, figury[figura])
            talia_lista.append(karta)

    return talia_lista


def hit_or_stay():
    """Decyzja o dalszym dokładaniu kart"""

    decision = input("Chcesz dalej dokładać karty? Wpisz 'T' lub 'N':")
    return decision


def bet():
    """Określa kwotę betu"""

    amount = input("Ile chciałłbyś postawić? Wpisz kwotę:")
    return int(amount)


def tasuj(talia):
    """Tasuje talię"""

    random.shuffle(talia)

    return talia


def imie_gracza():
    """Nadanie imienia graczowi, wyświetlenie powitania"""
    imie = input("Witaj w grze Blackjack, jak się nazywasz?")
    print(
        f"Cześć {imie}. Będziesz grał przeciwko komputerowi o imieniu Bernard. Powodzenia!"
    )
    gracze = [imie, "Bernard"]

    return gracze


def starting_bankroll(gracz, komputer):
    """Określenie depozytu początkowego"""

    numbers = "0123456789"
    validformat = False
    while validformat == False:
        suma = input("Jaką kwotę pieniędzy przyznać na początku każdemu z graczy?")
        validformat = True
        for i in suma:
            if i not in numbers:
                validformat = False
                print("Początkowa kwota musi być liczbą dodatnią! Spróbuj jeszcze raz!")
                break
        if suma == "0":
            print("Kwota nie może być równa 0! Spróbuj jeszcze raz!")
            validformat = False

    print(f"Depozyt gacza {gracz} został zasilony kwotą {suma} $.")
    print(f"Depozyt komputera {komputer} został zasilony kwotą {suma} $.")

    return int(suma)


def suma_gracza_check(gracz, sumka, przeciwnik, pula):
    """Monitorowanie sumy kart gracza"""

    if sumka > 21:
        print(
            f"Suma gracza {gracz} przekroczyła 21 punktów i wynosi {sumka}. {przeciwnik} wygrywa i zgarnia {pula} $."
        )
        return False
    else:
        return True


def stawkafn(graczdepo, komputerdepo):
    """Określenie stawki danej partii"""

    lista = list((graczdepo, komputerdepo))
    numbers = "0123456789"
    kwota = False
    while kwota == False:
        stawka = input("Jaką kwotę chciałbyś postawić?")
        kwota = True
        for x in stawka:
            if x not in numbers:
                print("Kwota stawki musi być liczbą dodatnią!")
                kwota = False
    if int(stawka) <= komputerdepo and int(stawka) <= graczdepo:
        return int(stawka)
    else:
        print(
            f"Zbyt duża kwota! Stawka nie może przekraczać depozytu gracza z najmniejszymi środkami. Wybierz kwotę od 0 do {min(lista)}."
        )
