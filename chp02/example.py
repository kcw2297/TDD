class Dollar:
    def __init__(self, value: int):
        self.amount = value
    
    def times(self, multiplier: int) -> 'Dollar':
        return Dollar(self.amount * multiplier)