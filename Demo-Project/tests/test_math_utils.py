from math_utils import add, subtract, pad_number

def test_add():
    result = add(2, 3)
    assert result == 5

def test_subtract():
    result = subtract(10, 3)
    assert result == 7

def test_add_negative():
    result = add(2, -3)
    assert result == -1

def test_subtract_negative():
    result = subtract(2, 3)
    assert result == -1

def test_pad_num():
    result = pad_number(5)
    assert result == '005'
    
    result = pad_number(123)
    assert result == '123'
    
    result = pad_number(0)
    assert result == '000'