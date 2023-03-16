import pytest
from main import multiply
def test_multiply_positive_numbers():
    assert multiply(2, 3) == 6
    assert multiply(0.5, 4) == 2
    assert multiply(100, 0.01) == 1

def test_multiply_negative_numbers():
    assert multiply(-2, 3) == -6
    assert multiply(0.5, -4) == -2
    assert multiply(-100, -0.01) == 1

def test_multiply_zero():
    assert multiply(0, 100) == 0
    assert multiply(0, -1) == 0
    assert multiply(0, 0) == 0

