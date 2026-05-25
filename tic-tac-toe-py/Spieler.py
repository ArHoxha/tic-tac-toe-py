class Spieler:
    def __init__(self, name: str, symbol: str):
        if not isinstance(name, str):
            raise TypeError("name muss ein String sein")
        if not isinstance(symbol, str) or len(symbol) != 1:
            raise ValueError("symbol muss ein einzelnes Zeichen sein")

        self._name = name
        self._symbol = symbol

    def get_name(self) -> str:
        return self._name

    def get_symbol(self) -> str:
        return self._symbol

    def __str__(self) -> str:
        return f"Spieler(name={self._name}, symbol={self._symbol})"


