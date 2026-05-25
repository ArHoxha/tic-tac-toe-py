class Spielfeld:
    def __init__(self):
        self.felder: list[list[str]] = [['-' for _ in range(3)] for _ in range(3)]

    def feld(self) -> None:
        for i in range(len(self.felder)):
            for j in range(len(self.felder[i])):
                self.felder[i][j] = '-'

    def zeige_spielfeld(self) -> None:
        for zeile in self.felder:
            print(' '.join(zeile))

    def setze_symbol(self, x: int, y: int, symbol: str) -> bool:
        if (
            0 <= x < 3
            and 0 <= y < 3
            and self.felder[x][y] == '-'
            and isinstance(symbol, str)
            and len(symbol) == 1
        ):
            self.felder[x][y] = symbol
            return True
        return False

    def pruefe_verlust(self, symbol: str) -> bool:
        rows = len(self.felder)
        cols = len(self.felder[0])

        # Zeilen
        for i in range(rows):
            for j in range(cols - 2):
                if (
                    self.felder[i][j] == symbol
                    and self.felder[i][j + 1] == symbol
                    and self.felder[i][j + 2] == symbol
                ):
                    return True

        # Spalten
        for j in range(cols):
            for i in range(rows - 2):
                if (
                    self.felder[i][j] == symbol
                    and self.felder[i + 1][j] == symbol
                    and self.felder[i + 2][j] == symbol
                ):
                    return True

        # Diagonalen
        for i in range(rows - 2):
            for j in range(cols - 2):
                if (
                    self.felder[i][j] == symbol
                    and self.felder[i + 1][j + 1] == symbol
                    and self.felder[i + 2][j + 2] == symbol
                ):
                    return True

        # Rückwärtsdiagonale
        for i in range(rows - 2):
            for j in range(2, cols):
                if (
                    self.felder[i][j] == symbol
                    and self.felder[i + 1][j - 1] == symbol
                    and self.felder[i + 2][j - 2] == symbol
                ):
                    return True

        return False
