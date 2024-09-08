def sum(a,b):
    return a+b

def substract(a,b):
    return a-b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("La división por cero no está permitida")
    return a / b