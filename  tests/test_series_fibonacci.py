import pytest
from math_series.series import fibonacci

def test_one():
    actual= fibonacci(1)
    expected=1
    assert actual == expected 

def test_two():
    actual= fibonacci(2)
    expected=1
    assert actual == expected 

def test_three():
    actual= fibonacci(3)
    expected=2
    assert actual == expected 


def test_six():
    actual= fibonacci(6)
    expected=8
    assert actual == expected 

def test_string():
    actual= fibonacci('string')
    expected='please enter number'
    assert actual == expected 
    
def test_number_string():
    actual= fibonacci('1')
    expected=1
    assert actual == expected 