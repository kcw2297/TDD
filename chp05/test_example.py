from example import Dollar, Franc

def test_multiplication():
    dollar_instance = Dollar(5)
    assert Dollar(10).equals(dollar_instance.times(2))
    assert Dollar(15).equals(dollar_instance.times(3))
    
def test_franc_multiplication():
    franc_instance = Franc(5)
    assert Franc(10).equals(franc_instance.times(2))
    assert Franc(15).equals(franc_instance.times(3))
    
def testEquality():
    dollar_instance = Dollar(5)
    assert dollar_instance.equals(Dollar(5))
    assert not dollar_instance.equals(Dollar(6))