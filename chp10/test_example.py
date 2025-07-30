from example import Dollar, Franc, Money

def test_currency():
    assert Money.dollar(1).currency() == 'USD'
    assert Money.franc(1).currency() == 'CHF'

def test_multiplication():
    dollar_instance = Money.dollar(5)
    assert Dollar(10, 'USD').equals(dollar_instance.times(2))
    assert Dollar(15, 'USD').equals(dollar_instance.times(3))
    
def test_franc_multiplication():
    franc_instance = Franc(5, 'CHF')
    assert Franc(10, 'CHF').equals(franc_instance.times(2))
    assert Franc(15, 'CHF').equals(franc_instance.times(3))
    
def testEquality():
    franc_instance = Franc(5, 'CHF')
    assert Money.dollar(5).equals(Dollar(5, 'USD'))
    assert not Money.dollar(5).equals(Dollar(6, 'USD'))
    assert not Money.dollar(5).equals(Franc(5, 'CHF'))
    assert franc_instance.equals(Franc(5, 'CHF'))
    assert not franc_instance.equals(Franc(6, 'CHF'))