import math_func
import pytest

@pytest.mark.number
def test_add():
    assert math_func.add(7,3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7

@pytest.mark.number
def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10
    assert math_func.product(7) == 14

@pytest.mark.strings
def test_add_strings():
    result=math_func.add('Hello',' World')
    assert result == 'Hello World'
    assert type(result) is  str
    assert 'XXX' not in result

@pytest.mark.strings
def test_product_strings():
    result = 'Hello Hello '
    assert math_func.product('Hello ') == result
    assert type(result) is str
    assert 'ello' in result
