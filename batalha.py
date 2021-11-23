from rolador_de_dados_rpg import d20 # Puxa função do dado d20 do arquivo rolador_de_dados_rpg

def batalha_rapida_facil(personagem, vilao):  # Declara função de batalha rapida fácil
    
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

def batalha_rapida_media(personagem, vilao):  # Declara função de batalha rapida média
    
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

def batalha_rapida_dificil(personagem, vilao):  # Declara função de batalha rapida dificil
    
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