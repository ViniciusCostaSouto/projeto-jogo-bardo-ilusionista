from random import choice       # Comando responsável por sortear um valor dentro do array

def d4():                       # Cria a função referente a um dado de 4 lados
    d4 = []                     # Cria array vazio
    for i in range(1,5,1):      # Esse for vai fazer uma varredura e adicionar todos os lados do dado no array
        d4.append(i)            # Essa linha é responsável por adicionar o index atual do for no array
    resultado = choice(d4)      # Essa linha pega o array d4 e sorteia um valor dentro dele, que é como se você rolasse o dado
    return resultado            # Essa linha retorna o valor do resultado obtido para o código, ou seja, o valor que deu no dado

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