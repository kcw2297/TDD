from example import Dollar

def test_multiplication():
    dollar_instance = Dollar(5)
    assert Dollar(10).equals(dollar_instance.times(2))
    assert Dollar(15).equals(dollar_instance.times(3))
    
    
def testEquality():
    dollar_instance = Dollar(5)
    assert dollar_instance.equals(Dollar(5))
    assert not dollar_instance.equals(Dollar(6))