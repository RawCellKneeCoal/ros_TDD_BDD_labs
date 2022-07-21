# LAB BY ROSELE
import pytest

def divide(a, b):
    return a / b

#print(divide(5, 0))

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        print("Trying to do division by 0")
        divide(5, 0)