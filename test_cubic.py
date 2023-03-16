import pytest
from main import cubic

def test_cubic():
    assert cubic(2) == 8
    assert cubic(3) == 27
    assert cubic(-2) == -8
