from example import Dollar

def test_multiplication():
    dollar_instance = Dollar(5)
    product = dollar_instance.times(2)
    assert product.amount == 10
    new_prodct = dollar_instance.times(3)
    assert new_prodct.amount == 15