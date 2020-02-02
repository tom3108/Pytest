import math_func
import pytest

def test_add():
    assert math_func.add(7,3) == 10


def test_add_strings():
    result=math_func.add('Hello',' World')
    assert result == 'Hello World'


def test_add_float():
    assert math_func.add(7.5,3.5) == 11
