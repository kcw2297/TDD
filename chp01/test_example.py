from example import Dollar

def test_multiplication():
    dollar_instance = Dollar(5)
    dollar_instance.times(2)
    assert dollar_instance.amount == 10