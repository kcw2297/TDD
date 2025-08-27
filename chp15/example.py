from abc import abstractmethod

class Expression:
    @abstractmethod    
    def reduce(self, bank: "Bank", to: str) -> 'Money':
        pass
    
    @abstractmethod
    def plus(self, added: "Expression") -> 'Expression':
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

    def times(self, multiplier: int) -> Expression:
        return Money(self.amount * multiplier, self._currency)
    
    def plus(self, addend: Expression) -> Expression:
        return Sum(self, addend)
    
    def reduce(self, bank: 'Bank',  to: str) -> 'Money':
        rate = bank.rate(self._currency, to)
        return Money(self.amount // rate, to)
    
class Bank:
    def __init__(self):
        self.rates = {}
    
    def add_rate(self, source: str, to: str, rate:int) -> None:
        self.rates[Pair(source, to)] = rate
    
    def rate(self, source: str, to: str):
        if source == to: return 1
        return self.rates[Pair(source, to)]
    
    def reduce(self, source: Expression, to: str) -> Money:
        return source.reduce(self, to)

    
class Sum(Expression):
    def __init__(self, augend: Expression, addend: Expression):
        self.augend = augend
        self.addend = addend
        
    def reduce(self, bank: "Bank", to: str) -> Money:
        amount = self.augend.reduce(bank, to).amount + self.addend.reduce(bank, to).amount
        return Money(amount, to)
    
    def plus(self, addedd: Expression) -> Expression:
        return  # TODO: 다음 챕처를 위한 stub
    
class Pair():
    def __init__(self, source: str, to: str):
        self.source = source
        self.to = to
    
    def __eq__(self, other: "Pair") -> bool:
        return self.source == other.source and self.to == other.to
    
    def __hash__(self) -> int:
        return hash((self.source, self.to))
        
        