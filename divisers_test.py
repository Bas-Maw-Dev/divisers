from divisers import diviser

def test_returns_positive_integer():
    assert diviser(1) == 1
    
def test_correct_when_one():
    assert diviser(1) == 1

def test_correct_when_two():
    assert diviser(2) == 2

def test_correct_when_three():
    assert diviser(3) == 1