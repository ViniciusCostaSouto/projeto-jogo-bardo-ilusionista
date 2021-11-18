from rolador_de_dados_rpg import d20

def batalha_rapida_facil(personagem, vilao):
    
    resultado = []
    i = 0
    while i != 5:
      rolagem_do_player = d20()
      rolagem_do_vilao = d20()
        
      if rolagem_do_player >= rolagem_do_vilao:
            resultado.append('P')
      elif rolagem_do_vilao > rolagem_do_player:
            resultado.append('V')
      i += 1
    resultado_personagem = resultado.count('P')
    resultado_vilao = resultado.count('V')

    if resultado_personagem > resultado_vilao:
      return True
    elif resultado_personagem < resultado_vilao:
      return False

def batalha_rapida_media(personagem, vilao):
    
    resultado = []
    i = 0
    while i != 10:
      rolagem_do_player = d20()
      rolagem_do_vilao = d20()
        
      if rolagem_do_player >= rolagem_do_vilao:
            resultado.append('P')
      elif rolagem_do_vilao > rolagem_do_player:
            resultado.append('V')
      i += 1
    resultado_personagem = resultado.count('P')
    resultado_vilao = resultado.count('V')

    if resultado_personagem > resultado_vilao:
      return True
    elif resultado_personagem < resultado_vilao:
      return False

def batalha_rapida_dificil(personagem, vilao):
    
    resultado = []
    i = 0
    while i != 15:
      rolagem_do_player = d20()
      rolagem_do_vilao = d20()
        
      if rolagem_do_player >= rolagem_do_vilao:
            resultado.append('P')
      elif rolagem_do_vilao > rolagem_do_player:
            resultado.append('V')
      i += 1
    resultado_personagem = resultado.count('P')
    resultado_vilao = resultado.count('V')

    if resultado_personagem > resultado_vilao:
      return True
    elif resultado_personagem < resultado_vilao:
      return False