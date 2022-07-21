# LAB BY ROSELE
import pytest

class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()

# print(calc.add(1, 1))

def test_add1():
    assert calc.add(1,1) == 2

def test_add2():
    assert calc.add(1.0,2.5) == 3.5

def test_add3():
    assert calc.add(0,0) == 0

def test_add4():
    assert calc.add(-5,-6) == -11