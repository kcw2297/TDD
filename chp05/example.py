class Dollar:
    def __init__(self, value: int):
        self.amount = value
    
    def times(self, multiplier: int) -> 'Dollar':
        return Dollar(self.amount * multiplier)
    
    def equals(self, dollar: 'Dollar'):
        return self.amount == dollar.amount
    
class Franc:
    def __init__(self, value: int):
        self.amount = value
    
    def times(self, multiplier: int) -> 'Franc':
        return Franc(self.amount * multiplier)
    
    def equals(self, dollar: 'Franc'):
        return self.amount == dollar.amount
    