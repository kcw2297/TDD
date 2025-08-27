from example import  Money, Bank, Sum

def test_currency():
    assert Money.dollar(1).currency() == 'USD'
    assert Money.franc(1).currency() == 'CHF'

def test_multiplication():
    dollar_instance = Money.dollar(5)
    result1 = dollar_instance.times(2)
    assert isinstance(result1, Money) and Money.dollar(10).equals(result1)
    result2 = dollar_instance.times(3)
    assert isinstance(result2, Money) and Money.dollar(15).equals(result2)
    
def test_simple_addition():
    five = Money.dollar(5)
    sum = five.plus(five)
    bank = Bank()
    reduced = bank.reduce(sum, 'USD')
    
    assert reduced.amount == Money.dollar(10).amount

def test_plus_return_sum():
    five = Money.dollar(5)
    sum = five.plus(five)
    assert isinstance(sum, Sum)
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
    

def test_identity_rate():
    bank = Bank()
    assert 1 == bank.rate("USD", "USD")

    
def test_reduce_money_different_currency():
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    result = bank.reduce(Money.franc(2), "USD")
    
    assert Money.dollar(1).amount == result.amount
    
    
def test_mixed_addition():
    fiveBucks = Money.dollar(5)
    tenFrancs = Money.franc(10)
    
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    
    result = bank.reduce(fiveBucks.plus(tenFrancs), 'USD')
    
    assert Money.dollar(10).amount == result.amount
    
    
    