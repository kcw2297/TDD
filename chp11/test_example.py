from example import  Money

def test_currency():
    assert Money.dollar(1).currency() == 'USD'
    assert Money.franc(1).currency() == 'CHF'

def test_multiplication():
    dollar_instance = Money.dollar(5)
    assert Money(10, 'USD').equals(dollar_instance.times(2))
    assert Money(15, 'USD').equals(dollar_instance.times(3))
    
    
