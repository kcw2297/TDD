from abc import abstractmethod


class Money:
    def __init__(self, value: int, currency: str):
        self._amount = value
        self._currency = currency

    @staticmethod
    def dollar(amount: int):
        return Dollar(amount, 'USD')

    @staticmethod
    def franc(amount: int):
        return Franc(amount, 'CHF')

    @abstractmethod
    def times(self, multiplier: int):
        return

    def equals(self, money: 'Money'):
        return self._amount == money._amount and type(self) == type(money)

class Dollar(Money):
    def __init__(self, value: int, currency: str):
        super().__init__(value, currency)
    
    def times(self, multiplier: int) -> Money:
        return Money.dollar(self._amount * multiplier)

    def currency(self) -> str:
        return self._currency
    
class Franc(Money):
    def __init__(self, value: int, currency: str):
        super().__init__(value, currency)
    
    def times(self, multiplier: int) -> Money:
        return Money.franc(self._amount * multiplier)
    
    def currency(self) -> str:
        return self._currency
    
    