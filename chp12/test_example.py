from example import  Money, Bank

def test_currency():
    assert Money.dollar(1).currency() == 'USD'
    assert Money.franc(1).currency() == 'CHF'

def test_multiplication():
    dollar_instance = Money.dollar(5)
    assert Money.dollar(10).equals(dollar_instance.times(2))
    assert Money.dollar(15).equals(dollar_instance.times(3))
    
def test_simple_addition():
    five = Money.dollar(5)
    sum = five.plus(Money.dollar(5))
    bank = Bank()
    reduced = bank.reduce(sum, 'USD')
    
    assert reduced.amount == Money.dollar(10).amount
