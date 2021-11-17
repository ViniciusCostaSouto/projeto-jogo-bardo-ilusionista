from rolador_de_dados_rpg import d4
from rolador_de_dados_rpg import d6
from rolador_de_dados_rpg import d8
from rolador_de_dados_rpg import d10
from rolador_de_dados_rpg import d12
from rolador_de_dados_rpg import d20
from rolador_de_dados_rpg import d100

def teste_dificuldade_1():
    dificuldade = 4
    rolagem = d8()

    if rolagem > dificuldade:
        return True
    else:
        return False

def teste_dificuldade_2():
    dificuldade = 6
    rolagem = d10()

    if rolagem > dificuldade:
        return True
    else:
        return False

def teste_dificuldade_3():
    dificuldade = 12
    rolagem = d20()

    if rolagem > dificuldade:
        return True
    else:
        return False

def teste_dificuldade_4():
    dificuldade = 60
    rolagem = d100()

    if rolagem > dificuldade:
        return True
    else:
        return False

#def batalha_simples(personagem):

#def batalha_media(personagem):

#def batalha_dificil(personagem):