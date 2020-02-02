import math_func
import pytest

@pytest.mark.parametrize('n1, n2, result',
                         [
                             (7,3,10),
                             ("Hello"," World",'Hello World'),
                             (10.5, 2.5, 13)
                         ]
                         )
def test_add(n1, n2, result):
    assert math_func.add(n1 ,n2) == result


