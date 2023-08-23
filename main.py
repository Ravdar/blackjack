from karta import Karta
from gracz import Gracz
from utils import utworz_talie, imie_gracza, starting_bankroll, tasuj, stawkafn


def blackjack():
    """Rozgrywka w blackjacka"""

    talia = utworz_talie()  # zwraca talię 52 kart na podstawie classy Karta
    potasowana_talia = tasuj(talia)  # zwraca tę samą talię

    gracze = (
        imie_gracza()
    )  # input imienia, zwraca dwuelementową listę, pierwszy to imię gracza, druga imię dealera computera
    kwota_startowa = starting_bankroll(
        gracze[0], gracze[1]
    )  # input kwoty startowej, zwraca int, ograniczyć do intów dodatnich

    # zdefiniowanie gracza i dealera na podstawie klas z atrybutami z powyższych inputów
    gracz = Gracz(gracze[0], kwota_startowa, [])
    komputer = Gracz("Bernard", kwota_startowa, [])

    runda = 1

    # start pętli, która zamknie się dopiero wtedy kiedy komputer lub gracz będzie miał zero lub - na koncie
    while gracz.bankrut() == False and komputer.bankrut() == False:

        print(f"Runda {runda}")
        runda += 1

        # zeruje talie gracza i komputera
        gracz.karty = []
        komputer.karty = []

        # komunikat o aktualnym stanie depozytów
        print(f"Depozyt gracza {gracz.imie} wynosi {gracz.bankroll}$.")
        print(f"Depozyt gracza {komputer.imie} wynosi {komputer.bankroll}$.")

        # rozdanie kart z potasowanej talii graczowi i komputerowi
        gracz.karty.append(potasowana_talia.pop(0))
        gracz.karty.append(potasowana_talia.pop(0))
        komputer.karty.append(potasowana_talia.pop(0))
        komputer.karty.append(potasowana_talia.pop(0))

        # wyswietlenie kart i podsumowanie punktów graczowi
        print(
            f"Karty gracza {komputer.imie}: {komputer.karty[0].figura} {komputer.karty[0].kolor}, X"
        )
        print(
            f"Twoje karty: {gracz.karty[0].figura} {gracz.karty[0].kolor}, {gracz.karty[1].figura} {gracz.karty[1].kolor}. Suma punktów wynosi {gracz.karty[0].ranga + gracz.karty[1].ranga}."
        )

        # zapytanie o stawkę zakładu, tutaj trzeba nałożyć limity, niewięcej niż kwota, którą posiada najbiedniejszy gracz
        stawka = stawkafn(gracz.bankroll, komputer.bankroll)

        # kolejna petla robiąca wszelkie rzeczy do momentu zakończenia partii wygraną jednego z graczy
        won = False
        decision = "Default decision"
        while won == False:

            # kolejna pętla pytająca gracza o to czy chce dodać karty, aż do momentu aż wpiszę "N" lub wyrzuci go z poprzedniej pętli
            while decision != "N":
                decision = input(
                    f"Suma twoich kart daje {gracz.punkty_gracza()}. Czy chcesz dołożyć kartę? Wpisz 'T' lub 'N'."
                )
                if decision == "T":
                    gracz.karty.append(potasowana_talia.pop(0))
                    print(
                        f"Wyciągnięto kartę {gracz.karty[-1].kolor} {gracz.karty[-1].figura}."
                    )
                    # co jesli karta jest asem
                    if gracz.karty[-1].figura == "As" and gracz.punkty_gracza() > 21:
                        gracz.karty[-1].rank = 1
                    # co jesli wyciagając nową kartę, gracz przekroczy 21 pkt:komunikato wygranej komputera, dzialania na bankrollu, karty zwracane do talii
                    elif gracz.punkty_gracza() > 21:
                        print(
                            f"Suma twoich kart daje {gracz.punkty_gracza()}. Przegrywasz tę partię!"
                        )
                        gracz.bankroll = gracz.bankroll - stawka
                        komputer.bankroll = komputer.bankroll + stawka
                        potasowana_talia += gracz.karty
                        potasowana_talia += komputer.karty
                        won = True
                        break

                elif decision == "N":
                    while won == False:
                        if int(komputer.punkty_gracza()) > 21:
                            print(
                                f" Karty gracza Bernard: {komputer.pokaz_karty()}. Suma punktów przekroczyła 21 i wynosi {komputer.punkty_gracza()}.{gracz.imie} wygrywa tę partię!"
                            )
                            gracz.bankroll = gracz.bankroll + stawka
                            komputer.bankroll = komputer.bankroll - stawka
                            potasowana_talia += gracz.karty
                            potasowana_talia += komputer.karty
                            won = True
                        elif gracz.punkty_gracza() < komputer.punkty_gracza():
                            print(
                                f"Twoje karty: {gracz.pokaz_karty()}. Suma punktów wynosi {gracz.punkty_gracza()}."
                            )
                            print(
                                f"Karty Bernarda: {komputer.pokaz_karty()}. Suma punktów wynosi {komputer.punkty_gracza()}."
                            )
                            print(
                                f"{komputer.imie} wygrywa i zgarnia {int(stawka)*2}$."
                            )
                            gracz.bankroll = gracz.bankroll - stawka
                            komputer.bankroll = komputer.bankroll + stawka
                            potasowana_talia += gracz.karty
                            potasowana_talia += komputer.karty
                            won = True
                        elif (
                            gracz.punkty_gracza() == 21
                            and komputer.punkty_gracza() == 21
                        ):
                            print(
                                f"Twoje karty: {gracz.pokaz_karty()}. Suma punktów wynosi {gracz.punkty_gracza()}."
                            )
                            print(
                                f"Karty Bernarda: {komputer.pokaz_karty()}. Suma punktów wynosi {komputer.punkty_gracza()}."
                            )
                            print(
                                "REMIS! Obydwaj gracze uzyskali sumę punktów równą 21."
                            )
                            potasowana_talia += gracz.karty
                            potasowana_talia += komputer.karty
                            won = True
                        else:
                            komputer.karty.append(potasowana_talia.pop(0))

                else:
                    print("Wprowadziłeś niepoprawne dane! Wpisz 'T' lub 'N'.")


blackjack()
