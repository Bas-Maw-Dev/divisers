from divisers import diviser

def test_returns_positive_integer():
    assert diviser(1) == 1

def test_correct_when_one():
    assert diviser(1) == 1

def test_correct_when_two():
    assert diviser(2) == 2  # 2, 1

def test_correct_when_three():
    assert diviser(3) == 2  # 3, 1

def test_correct_when_four():
    assert diviser(4) == 3  # 4, 2, 1

def test_correct_when_five():
    assert diviser(5) == 2 # 5, 1
    
'''
def test_correct_when_six():
    assert diviser(6) == 4 # 6, 3, 2, 1 
'''