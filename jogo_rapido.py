from random import choice
from livro import ler_livro
from datetime import date 
from time import sleep
import calendar
from rolador_de_dados_rpg import d4
from rolador_de_dados_rpg import d6
from rolador_de_dados_rpg import d8
from rolador_de_dados_rpg import d10
from rolador_de_dados_rpg import d12
from rolador_de_dados_rpg import d20
from rolador_de_dados_rpg import d100
from teste_de_dificuldade import teste_dificuldade_1 as td1
from teste_de_dificuldade import teste_dificuldade_3 as td3
from quests_jogo_rapido import quest_principal

nomes = ["Amélie", "Pitão", "Tereza","Tom", "Ravena", "Latrel", "Estelar", "Brihanna", "Amigão", "Pade", "Kvothe", "Denna", "Auri"]
raças = ["Hobbit", "Anão", "Humano", "Draconato", "Elfo", "Felino", "Doguineo"]
classes = ["Guerreiro(a)", "Berserk", "Mago(a)", "Bardo(a)", "Monge(ja)", "Druida", "Analista de Dados"]

p1 = [choice(nomes), choice(raças), choice(classes)]
p2 = [choice(nomes), choice(raças), choice(classes)]
p3 = [choice(nomes), choice(raças), choice(classes)]
p4 = [choice(nomes), choice(raças), choice(classes)]
p5 = [choice(nomes), choice(raças), choice(classes)]

def taverneiro():    # Função para definir quem é o taverneiro da guilda de acordo com o dia atual
    my_date = date.today()
    dia_atual = calendar.day_name[my_date.weekday()]
    if dia_atual in ('Sunday', 'Tuesday','Thursday', 'Saturday'):
        taverneiro = 'Thraundir'
        return taverneiro
    elif dia_atual in ('Monday', 'Wednesday', 'Friday'):
        taverneiro = 'Rhogar'
        return taverneiro

def escolha_de_personagens(escolha_do_player):
    if int(escolha_do_player) == 1:
        sleep(1)
        print(f"\nVocê convidou {p1[0]} para sua aventura!\n")
        return p1
    elif int(escolha_do_player) == 2:
        sleep(1)
        print(f"\nVocê convidou {p2[0]} para sua aventura!\n")
        return p2
    elif int(escolha_do_player) == 3:
        sleep(1)
        print(f"\nVocê convidou {p3[0]} para sua aventura!\n")
        return p3
    elif int(escolha_do_player) == 4:
        sleep(1)
        print(f"\nVocê convidou {p4[0]} para sua aventura!\n")
        return p4
    elif int(escolha_do_player) == 5:
        sleep(1)
        print(f"\nVocê convidou {p5[0]} para sua aventura!\n")
        return p5

def lista_de_personagens():
    print("\nPersonagens disponíveis no momento na taverna: \n")

    personagem_1 = print(f"\n[1] Nome: {p1[0]} \n Raça: {p1[1]} \n Classe: {p1[2]}\n")
    personagem_2 = print(f"[2] Nome: {p2[0]} \n Raça: {p2[1]} \n Classe: {p2[2]}\n")
    personagem_3 = print(f"[3] Nome: {p3[0]} \n Raça: {p3[1]} \n Classe: {p3[2]}\n")
    personagem_4 = print(f"[4] Nome: {p4[0]} \n Raça: {p4[1]} \n Classe: {p4[2]}\n")
    personagem_5 = print(f"[5] Nome: {p5[0]} \n Raça: {p5[1]} \n Classe: {p5[2]}\n")

    personagem_escolhido = input("\nQual personagem você deseja convidar para a aventura? ")
    
    while personagem_escolhido not in {"1","2","3","4","5"}:
        personagem_escolhido = input("\nQual personagem você deseja convidar para a aventura? ")

    p_principal = escolha_de_personagens(int(personagem_escolhido))
    historia_inicial_quarto(p_principal)

def historia_inicial_quarto(p_escolhido):
    sleep(1)
    print(f"{p_escolhido[0]} acorda em seu quarto temporário na grandiosa taverna Triângulo Dourado se sentindo ")
    sleep(1)
    print(f"completamente revigorado(a) após sua última aventura da Guilda Dos Aventureiros. {p_escolhido[0]}, o(a) ")
    sleep(1)
    print(f"{p_escolhido[2]} levanta e começa a vestir sua armadura e se arrumar para sua próxima aventura pela ")
    sleep(1)
    print("Guilda.")
    sleep(1)
    print("")
    sleep(1)
    print(f'Após se arrumar com todos seus itens {p_escolhido[0]} se prepara para sair do quarto, porém pela primeira ')
    sleep(1)
    print(f'vez se depara com um livro que está em cima da escrivaninha. Na capa é possível observar algumas ')
    sleep(1)
    print(f'gravuras, essas marcas estão em uma língua diferente. Você acredita que já viu aquilo em algum ')
    sleep(1)
    print(f'lugar. ')
    sleep(1)
    print('')
    escolha_do_player = input("Você quer fazer um teste para ver se entende o que está escrito? ([1] Sim ou [2] Não) ")
    print('')
    while escolha_do_player not in {"1","2"}:
        escolha_do_player = input("\nVocê quer fazer um teste para ver se entende o que está escrito? ([1] Sim ou [2] Não) ")
    print('')
    if int(escolha_do_player) == 1:
        if td1() == True:
            sleep(1)
            print(f'Parabéns! Você obteve sucesso no seu teste.\n')
            sleep(1)
            print(f'Após tentar um pouco, você se lembra que é uma lingua usada pelos anões e está escrito: ')
            sleep(1)
            print(f'"A Origem da Taverna Triângulo Dourado e a Formação da Guilda dos Aventureiros"')
            sleep(1)
            print(f'{p_escolhido[0]} pensa consigo "Mas que nome gigante, será que leio esse livro agora ou vou para o salão? ')
            sleep(1)
            escolha_do_player = input("\nVocê quer ler o livro ou deseja ir para o salão da taverna? ([1] Ler livro ou [2] Ir para o Salão) ")
            print('')
            while escolha_do_player not in {"1","2"}:
                escolha_do_player = input("Você quer ler o livro ou deseja ir para o salão da taverna? ([1] Ler livro ou [2] Ir para o Salão) ")
                print('')
            if int(escolha_do_player) == 1:    
                sleep(1)
                print(ler_livro())
                historia_inicial_salao(p_escolhido)
            elif int(escolha_do_player) == 2:
                sleep(1)
                historia_inicial_salao(p_escolhido)
        elif td1() == False:            
            sleep(1)
            print(f"Que pena, você falhou no teste.")
            print(f"\nApós tentar um pouco, você vê que não lembra de nada e decide ir para o salão da Taverna.")
            historia_inicial_salao(p_escolhido)
   
    elif int(escolha_do_player) == 2:
        sleep(1)
        historia_inicial_salao(p_escolhido)

def historia_inicial_salao(personagem):
    sleep(1)
    print(f"{personagem[0]} finaliza os preparativos e sai do quarto em direção as escadas para o salão principal da Taverna. ")
    sleep(1)
    print(f"Após descer as escadas, {personagem[0]} chega no salão principal da taverna e se depara com um lugar lotado de seres ")
    sleep(1)
    print(f"de todas as raças possíveis conversando, bebendo, rindo, gritando e muito mais. Tudo isso enquanto o bardo BRUSHY ONE ")
    sleep(1)
    print("STRING manda ver em seu violão com uma corda cantando alguma canção conhecida como CHICKEN IN THE CORN.")
    sleep(1)
    print("Você fica um tempo meio atordoado por conta de receber esse tanto de informação ao mesmo tempo. Porém, por mais que pareça ")
    sleep(1)
    print(f'que esteja um caos aquele lugar, você se sente feliz por estar ali e por ter dado tudo certo em sua última aventura. ')
    sleep(1)
    print(f'Mas como tudo bom dura pouco... Você ouve alguém gritando seu nome: ')
    sleep(1)
    print(f'\n???: "{personagem[0]}, finalmente você acordou, achei que você ia dormir pra sempre! Fiquei preocupado com você. Venha aqui,')
    sleep(1)
    print(f'vamos conversar!"\n')
    sleep(1)
    print(f'Você percebe que aquela voz é do taverneiro e co-criador da Guilda {taverneiro()} e decide seguir na direção dele para ver ')
    sleep(1)
    print(f'o que ele quer.')
    sleep(1)
    print(f'"\n{taverneiro()}: Jovem, fico feliz que tenha dado tudo certo em sua última aventura! Você está pronto(a) pra outra aventura?"\n')
    sleep(1)
    print(f'{personagem[0]}: Sim, estou animado(a) para voltar a ativa porque sinto que por mais que tenha voltado há apenas 5 dias, já ')
    sleep(1)
    print(f'estou sentindo acumulando teias de aranha em meu equipamento. Então, é hora de partir numa jornada. O que você teria de missão ')
    sleep(1)
    print(f'disponível para me oferecer Senhor {taverneiro()}?"\n')
    sleep(1)
    print(f'{taverneiro()} responde num tom meio sério e meio brincalhão: \n')
    sleep(1)
    print(f'{taverneiro()}: Não me venha com essa de senhor, eu não sou tão velho assim. Você sabe que pode me chamar só de {taverneiro()}.')
    sleep(1)
    print(f'Bem, brincadeiras a parte, tenho uma missão séria e estava procurando alguém de confiança para poder confiar essa quest em espe-')
    sleep(1)
    print(f'cífico. Quando soube que você havia retornado, tive certeza que seria o {personagem[1]} {personagem[2]} perfeito para realizar')
    sleep(1)
    print(f'essa quest.\n')
    sleep(1)
    print(f'{personagem[0]} fica meio envergonhado diante o elogio vindo de alguém tão importante e diz:\n')
    sleep(1)
    print(f'{personagem[0]}: Poxa, eu agradeço pela confiança {taverneiro()}! Mas afinal, que missão é essa que precisa de alguém tão especí-')
    sleep(1)
    print(f'fico e parece estar te preocupando tanto?"\n')
    sleep(1)
    print(f'\n{taverneiro()} chega mais próximo de {personagem[0]} e diz baixinho: ')
    sleep(1)
    print(f'\n{taverneiro()}: Você se lembra de como a Guilda foi formada? Então, diversas fontes minhas anônimas minhas vem me informando que ')
    sleep(1)
    print(f'ultimamente está começando a surgir um burburinho de que alguns soldados do exército de Dio sobreviveram e estão começando a reu-')
    sleep(1)
    print(f'nir seres que estão dispostos a segui-los na jornada para trazer Dio de volta. Fiquei sabendo que atualmente existem 5 campos des-')
    sleep(1)
    print(f'se espalhados por aí, e eu possuo a localização dos três. Sabendo disso, eu fiquei afim de ir atrás e encerrar isso eu mesmo, mas eu')
    sleep(1)
    print(f'fiz um juramento de que não ia mais entrar em batalhas em respeito ao sacríficio de Duncan. Por conta disso, precisava pensar em al-')
    sleep(1)
    print(f'guém louco o suficiente para topar partir numa missão maluca dessas. Você é esse alguém, e eu acredito que você tem o potencial para')
    sleep(1)
    print(f'limpar esses campos e encerrar de vez com essa loucura. E então, o que me diz {personagem[0]}? Acredita que essa missão esteja a sua altura?\n')
    sleep(1)
    
    escolha_do_player = input(f'\nO que {personagem[0]} deve fazer? [1] Aceita ir realizar a quest de {taverneiro()} ou [2] Não aceita a quest ')
    print('')
    
    while escolha_do_player not in {"1","2"}:
        escolha_do_player = input(f'\nO que {personagem[0]} deve fazer? [1] Aceita ir realizar a quest de {taverneiro()} ou [2] Não aceita a quest ')
        print('')
    
    if int(escolha_do_player) == 2:    
        print(f'{personagem[0]} fica com medo e tenta recusar a proposta e ir beber.')
        sleep(1)
        teste = td3()
        if teste == True:
            sleep(1)
            print(f'\nParabéns! Você obteve sucesso no seu teste.\n')
            sleep(1)
            print(f'{personagem[0]} agradece a proposta porém acha aquilo muito além de suas habilidades\n')
            sleep(1)
            print(f'{taverneiro()}: Fico chateado com isso, mas respeito sua escolha. No momento não temos missão nenhuma.\n')
            sleep(1)
            print(f'{personagem[0]} se senta em uma das mesas e começa a beber as cervejas da Taverna.\n')
            sleep(1)
            print(f'{personagem[0]} passa do ponto e fica altamente embriagado(a) e desmaia no bar.\n')
            sleep(1)
            print(f'Fim!\n')
            sleep(1)
            print(f'Muito obrigado por ter jogado, porém esse não é o final interessante! Se estiver curioso, tente novamente e aceite a quest! ;D\n')
            quit()
        elif teste == False:
            sleep(1)
            print(f'\nQue pena! Você falhou no seu teste.\n')
            sleep(1)
            print(f'{personagem[0]} diz que não aceita a missão porém {taverneiro()} exibe um olhar de reprovação e diz: \n')
            sleep(1)
            print(f'{taverneiro()}: É uma pena que você tenha agido dessa forma, acredito que tenha dito isso porque está com medo.')
            print("Mas só você é capaz de realizar essa missão, então aceitando ou não, você irá. Isso é uma ordem!")
            sleep(1)
            quest_principal(personagem,taverneiro())
    elif int(escolha_do_player) == 1:
        print(f'{personagem[0]} sente um ímpeto de justiça surgir em seu peito diz:\n')
        sleep(1)
        print(f'{personagem[0]}: Eu aceito essa missão {taverneiro()}! Vou atingir suas expectativas e resolver esse problema!')
        sleep(1)
        quest_principal(personagem,taverneiro())
    