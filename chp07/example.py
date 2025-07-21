class Money:
    def __init__(self, value: int):
        self._amount = value

    def equals(self, money: 'Money'):
        return self._amount == money._amount and type(self) == type(money)

class Dollar(Money):
    def __init__(self, value: int):
        super().__init__(value)
    
    def times(self, multiplier: int) -> 'Dollar':
        return Dollar(self._amount * multiplier)
    
class Franc(Money):
    def __init__(self, value: int):
        super().__init__(value)
    
    def times(self, multiplier: int) -> 'Franc':
        return Franc(self._amount * multiplier)