import pytest
from math_series.series import sum_series

def test_one():
    assert sum_series(1,2,1)==1
def test_three():
    assert sum_series(3,2,1)==4
def test_seven():
    assert sum_series(7,2,1)==29
def test_one_no_arg():
    assert sum_series(1)==1
def test_three_no_arg():
    assert sum_series(3)==2
def test_seven_no_arg():
    assert sum_series(7)==13    