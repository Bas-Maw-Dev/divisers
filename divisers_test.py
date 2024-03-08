from divisers import diviser
'''
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

def test_correct_when_six():
    assert diviser(6) == 4 # 6, 3, 2, 1 
    
def test_correct_when_seven():
    assert diviser(7) == 2 # 7, 1
    
def test_correct_when_eight():
    assert diviser(8) == 4 # 8, 4, 2, 1
    
def test_correct_when_nine():
    assert diviser(9) == 3 # 9, 3, 1
'''
def test_returns_positive_integer():
    assert diviser(1) == 1



def test_range_up_to_forty():
      
    for i in range(1, 41):
        number_return = 0
        for j in range(1,10):
            if i % j == 0:
                number_return += 1
        assert diviser(i) == number_return