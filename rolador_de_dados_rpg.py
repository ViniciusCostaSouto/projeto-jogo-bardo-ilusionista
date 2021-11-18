from random import choice

def d4():
    d4 = []
    for i in range(1,5,1):
        d4.append(i)
    resultado = choice(d4)
    return resultado

def d6():
    d6 = []
    for i in range(1,7,1):
        d6.append(i)
    resultado = choice(d6)
    return resultado

def d8():
    d8 = []
    for i in range(1,9,1):
        d8.append(i)
    resultado = choice(d8)
    return resultado

def d10():
    d10 = []
    for i in range(1,11,1):
        d10.append(i)
    resultado = choice(d10)
    return resultado

def d12():
    d12 = []
    for i in range(1,13,1):
        d12.append(i)
    resultado = choice(d12)
    return resultado

def d20():
    d20 = []
    for i in range(1,21,1):
        d20.append(i)
    resultado = choice(d20)
    return resultado

def d100():
    d100 = []
    for i in range(1,101,1):
        d100.append(i)
    resultado = choice(d100)
    return resultado