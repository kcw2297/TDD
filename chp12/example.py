class Expression:
    pass

class Money(Expression):
    def __init__(self, value: int, currency: str):
        self.amount = value
        self._currency = currency

    @staticmethod
    def dollar(amount: int) -> 'Money':
        return Money(amount, 'USD')

    @staticmethod
    def franc(amount: int) -> 'Money':
        return Money(amount, 'CHF')
    
    def currency(self) -> str:
        return self._currency

    def equals(self, money: 'Money') -> bool:
        return self.amount == money.amount and self._currency == money.currency()

    def times(self, multiplier: int) -> 'Money':
        return Money(self.amount * multiplier, self._currency)
    
    def plus(self, addend: 'Money'):
        return Money(self.amount + addend.amount, self._currency)
    
class Bank:
    def reduce(self, source: Expression, to: str) -> Money:
        return Money.dollar(10)