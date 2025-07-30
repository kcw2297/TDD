class Money:
    def __init__(self, value: int, currency: str):
        self._amount = value
        self._currency = currency

    @staticmethod
    def dollar(amount: int):
        return Money(amount, 'USD')

    @staticmethod
    def franc(amount: int):
        return Money(amount, 'CHF')

    def times(self, multiplier: int) -> 'Money':
        return Money(self._amount * multiplier, self._currency)
    
    def currency(self):
        return self._currency

    def equals(self, money: 'Money'):
        return self._amount == money._amount and self._currency == money.currency()

    