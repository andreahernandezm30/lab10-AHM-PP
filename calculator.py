# https://github.com/andreahernandezm30/lab10-AHM-PP.git 
# Partner 1: Prasheel Patel
# Partner 2: Andrea Hernandez Monserratte
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def subtract(a, b):
    return a - b

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("invalid logarithm base")
    if b <= 0:
        raise ValueError("log argument must be > 0")
    return math.log(b, a)

def exp(a, b):
    return a ** b
