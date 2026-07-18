# all mathematical operations
import math

def add(a , b):
    return a + b

def sub(a , b):
    return a - b

def mul(a , b):
    return a * b

def div(a , b):
    if b == 0:
        return "cannot divide by 0"
    return a / b

def sq(a):
    return a ** 2

def cube(a):
    return a ** 3

def power(a , b):
    return a ** b

def sq_rt(a):
    if a < 0:
        return "sq root of negative number is not possible"
    return math.sqrt(a)

def percent(a,b):
    return(a/b) * 100
