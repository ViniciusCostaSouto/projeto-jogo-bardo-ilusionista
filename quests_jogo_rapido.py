from random import choice
from teste_de_dificuldade import teste_dificuldade_1
from batalha import batalha_rapida_facil as brf
from batalha import batalha_rapida_media as brm
from batalha import batalha_rapida_dificil as brd
from time import sleep

lugar = ["Origem do Vento", "Costa do Falcão", "Vale de Dadaupa", "Montanha Aozang", "Planícies de Guili", "Relevo de Jueyun", "Cabeça da Serpente", "Lagoa Suigetsu", "Floresta Chinju"]
inimigos = ["Hilichurls", "Acólitos", "Soldados", "Bruxos", "Malucos", "Guerreiros Hipnotizados", "ቦልሶናሮ"]  

def sortear_lugar():
    lugar_sorteado = choice(lugar)
    return lugar_sorteado

def sortear_inimigo():
    inimigo_sorteado = choice(inimigos)
    return inimigo_sorteado

def quest_principal(personagem, taverneiro):
    primeiro_lugar_sorteado = sortear_lugar()
    segundo_lugar_sorteado = sortear_lugar()
    terceiro_lugar_sorteado = sortear_lugar()

    primeiro_inimigo_sorteado = sortear_inimigo()
    segundo_inimigo_sorteado = sortear_inimigo()
    terceiro_inimigo_sorteado = sortear_inimigo()
    sleep(1)
    print(f'\n{taverneiro}: Você não tem ideia do quanto me alegra ouvir essa resposta. Bom, não podemos perder')
    sleep(1)
    print('tempo com isso. Vou te passar logo os detalhes para você partir o mais rápido possível. E sobre a recom-')
    sleep(1)
    print('pensa, não se preocupe, você vai ser muito bem recompensado(a) por essa missão. Poderá até tirar um tem-')
    sleep(1)
    print('po de férias da Guilda para poder descansar e aproveitar bastante. Outra coisa, assim que finalizar essa')
    sleep(1)
    print('quest, assim que você retornar, terá um grande banquete e uma festa te aguardando! Bom, sem mais delongas,')
    sleep(1)
    print('vamos para o que interessa. São três campos principais que precisam ser detidos, assim que eles caírem, é ')
    sleep(1)
    print('apenas uma questão de tempo para que essa loucura acabe. As localizações e os inimigos que estão lá são: \n')
    sleep(1)
    print(f'\nPrimeiro Acampamento Inimigo: {primeiro_lugar_sorteado}, Inimigo: {primeiro_inimigo_sorteado}\n')
    sleep(2)
    print(f'\nSegundo Acampamento Inimigo: {segundo_lugar_sorteado}, Inimigo: {segundo_inimigo_sorteado}\n')
    sleep(2)
    print(f'\nTerceiro Acampamento Inimigo: {terceiro_lugar_sorteado}, Inimigo: {terceiro_inimigo_sorteado}\n')
    sleep(2)
    print(f'\n{personagem[0]} pega todo seu equipamento e parte em sua jornada em direção ao primeiro acampamento.\n')
    sleep(1)
    print('.\n')
    sleep(1)
    print('.\n')
    sleep(1)
    print('.')
    sleep(1)
    print(f'\n{personagem[0]} chega ao primeiro acampamento e se prepara na surdina para atacar.\n')
    sleep(1)
    print('.\n')
    sleep(1)
    print(f'\nDepois de se preparar, {personagem[0]} depois parte para atacar todos os {primeiro_inimigo_sorteado}.\n')
    sleep(1)
    batalha_campo_1 = brf(personagem[0], primeiro_inimigo_sorteado)

    if batalha_campo_1 == False:
        sleep(1)
        print("Que pena, você falhou no teste! :(\n")
        sleep(2)
        print(f'{personagem[0]} luta bravamente contra os {primeiro_inimigo_sorteado} porém acaba perdendo a batalha.')
        sleep(1)
        print("\nGame Over\n")
        quit()
    
    sleep(2)
    print("\nParabéns! Você obteve sucesso no seu teste.\n")
    sleep(2)
    print(f'{personagem[0]} luta bravamente contra os {primeiro_inimigo_sorteado} e derrota todos eles com seu poder ')
    sleep(1)
    print(f'e mostra que se tornou um {personagem[2]} muito forte, porém ainda tem dois campos para limpar. Ainda não é')
    sleep(1)
    print(f'hora para comemorar.\n')
    sleep(1)
    print('.\n')
    sleep(1)
    print('.\n')
    sleep(1)
    print('.')
    sleep(1)
    print(f'\n{personagem[0]} chega ao segunda acampamento e se prepara para atacar agora os {segundo_inimigo_sorteado}.\n')
    sleep(1)
    print('.\n')
    sleep(1)
    print(f'\nDepois de se preparar, {personagem[0]} depois parte para atacar todos os {segundo_inimigo_sorteado}.\n')
    sleep(1)
    batalha_campo_2 = brm(personagem[0], segundo_inimigo_sorteado)

    if batalha_campo_2 == False:
        sleep(1)
        print("Que pena, você falhou no teste! :(\n")
        sleep(2)
        print(f'{personagem[0]} luta bravamente contra os {segundo_inimigo_sorteado} porém acaba perdendo a batalha.')
        sleep(1)
        print("\nGame Over\n")
        quit()
    
    sleep(2)
    print("\nParabéns! Você obteve sucesso no seu teste.\n")
    sleep(2)
    print(f'{personagem[0]} luta ferozmente contra os {segundo_inimigo_sorteado} e derrota todos eles utilizando os ')
    sleep(1)
    print(f'poderes equipamentos que o deixaram muito forte, agora a vitória parece surgir no horizonte. Mas ainda não é')
    sleep(1)
    print(f'hora para comemorar, pois precisa partir logo pro terceiro e último acampamento.\n')
    sleep(1)
    print('.\n')
    sleep(1)
    print('.\n')
    sleep(1)
    print('.')
    sleep(1)
    print(f'\n{personagem[0]} chega ao último acampamento e se prepara para atacar agora os {terceiro_inimigo_sorteado}.\n')
    sleep(1)
    print('.\n')
    sleep(1)
    print(f'\nDepois de se preparar, {personagem[0]} depois parte para atacar todos os {terceiro_inimigo_sorteado}.\n')
    sleep(1)
    batalha_campo_3 = brd(personagem[0], terceiro_inimigo_sorteado)

    if batalha_campo_3 == False:
        sleep(1)
        print("Que pena, você falhou no teste! :(\n")
        sleep(2)
        print(f'{personagem[0]} luta bravamente contra os {terceiro_inimigo_sorteado} porém acaba perdendo a batalha.')
        sleep(1)
        print("\nGame Over\n")
        quit()
    
    sleep(2)
    print("\nParabéns! Você obteve sucesso no seu teste.\n")
    sleep(2)
    print(f'{personagem[0]} luta com todas as suas forças contra os {segundo_inimigo_sorteado} e derrota todos eles ')
    sleep(1)
    print(f'utilizando os poderes de sua classe {personagem[2]} que o deixaram muito forte. Após derrotar esse último')
    sleep(1)
    print(f'campo, finalmente se dá conta de que por mais que parecesse que o tempo passou rápido, na verdade havia se ')
    sleep(1)
    print(f'passado 3 meses desde que havia saído da Guilda em direção a {primeiro_lugar_sorteado}. E agora, com a mente ')
    sleep(1)
    print(f'tranquila e a consciência de que havia salvado o mundo. Decide retornar para a Guilda e finalmente poder curtir!')
    sleep(1)
    print('.\n')
    sleep(1)
    print('.\n')
    sleep(1)
    print('.')
    sleep(1)
    print(f'{personagem[0]} chega na Guilda 2 semanas depois da batalha de {terceiro_lugar_sorteado} e logo quando entra já')
    print(f'avista {taverneiro}, que o(a) vê também e parte em direção para te dar um abraço acalorado e grita para todos: \n')
    print(f'{taverneiro}: TRÊS URRAS PARA {personagem[0]}!!! QUE FOI QUEM SALVOU O MUNDO DAQUELES MALDITOS LOUCOS.')
    print('.\n')
    sleep(1)
    print('.\n')
    sleep(1)
    print('.')
    sleep(1)
    print("Fim de Jogo")
    sleep(1)
    print("Muito obrigado por ter jogado, espero que tenha se divertido!")
    sleep(1)
    quit()