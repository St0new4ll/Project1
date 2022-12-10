import math


def add(x, y):
    result = float(x) + float(y)
    return result


def subtract(x, y):
    result = float(x) - float(y)
    return result


def multiply(x, y):
    result = float(x) * float(y)
    return result


def divide(x, y):
    if y == 0:
        exit
    result = float(x) / float(y)
    return result


def RaiseTo(x, y):
    if y == 0:
        return 1
    result = float(x) ** float(y)
    return result


def sqr(x):
    result = x ** 2
    return result


def rect(x, y):
    result = x * y
    return result


def tri(x, y):
    result = (1/2) * x * y
    return result


def circ(x):
    result = math.pi * x ** 2
    return result

def ellip(x, y):
    result = math.pi * x * y
    return result

def cube(x):
    result = x**3
    return result


def cylin(x, y):
    result = math.pi * (x ** 2) * y
    return result


def prism(x, y):
    result = (x ** 2) * y
    return result

def sphere(x):
    result = (4/3) * math.pi * (x ** 3)
    return result

