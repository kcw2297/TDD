from example import  Money, Bank, Sum

def test_currency():
    assert Money.dollar(1).currency() == 'USD'
    assert Money.franc(1).currency() == 'CHF'

def test_multiplication():
    dollar_instance = Money.dollar(5)
    assert Money.dollar(10).equals(dollar_instance.times(2))
    assert Money.dollar(15).equals(dollar_instance.times(3))
    
def test_simple_addition():
    five = Money.dollar(5)
    sum = five.plus(five)
    bank = Bank()
    reduced = bank.reduce(sum, 'USD')
    
    assert reduced.amount == Money.dollar(10).amount

def test_plus_return_sum():
    five = Money.dollar(5)
    sum = five.plus(five)
    assert five == sum.augend
    assert five == sum.addend
    
def test_reduce_sum():
    sum = Sum(Money.dollar(3), Money.dollar(4))
    bank = Bank()
    result = bank.reduce(sum, "USD")
    assert Money.dollar(7).amount == result.amount    

def test_reduce_money():
    bank = Bank()
    result = bank.reduce(Money.dollar(1), 'USD')
    assert Money.dollar(1).amount == result.amount