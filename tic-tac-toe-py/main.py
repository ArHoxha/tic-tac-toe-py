from Spieler import Spieler
from Spielfeld import Spielfeld


def main() -> None:
    print("_____________________________________________")
    print("_________________Tic Tac Toe_________________")
    print("_____________________________________________")

    spielfeld = Spielfeld()
    spieler1 = Spieler("Spieler 1", "X")
    spieler2 = Spieler("Spieler 2", "O")
    aktueller_spieler = spieler1

    while True:
        spielfeld.zeige_spielfeld()
        print(f"{aktueller_spieler.get_name()} ({aktueller_spieler.get_symbol()}) ist dran.")

        try:
            x_str, y_str = input("Gib Zeile und Spalte ein (1-3), getrennt durch Leerzeichen: ").split()
            x = int(x_str) - 1
            y = int(y_str) - 1
        except ValueError:
            print("Ungültige Eingabe. Bitte zwei Zahlen von 1 bis 3 eingeben.")
            continue

        if not spielfeld.setze_symbol(x, y, aktueller_spieler.get_symbol()):
            print("Dieses Feld ist belegt oder ungültig. Versuche es erneut.")
            continue

        if spielfeld.pruefe_verlust(aktueller_spieler.get_symbol()):
            spielfeld.zeige_spielfeld()
            print(f"{aktueller_spieler.get_name()} hat gewonnen!")
            break

        if all(feld != '-' for reihe in spielfeld.felder for feld in reihe):
            spielfeld.zeige_spielfeld()
            print("Unentschieden!")
            break

        aktueller_spieler = spieler2 if aktueller_spieler == spieler1 else spieler1


if __name__ == "__main__":
    main()

