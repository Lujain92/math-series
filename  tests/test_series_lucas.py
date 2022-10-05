import pytest
from math_series.series import lucas

def test_one():
    assert lucas(1)==1
def test_three():
    assert lucas(3)==4
def test_seven():
    assert lucas(7)==29