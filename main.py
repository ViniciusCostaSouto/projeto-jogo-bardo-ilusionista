import jogo_rapido as jr
# from livro import ler_livro
from pyfiglet import Figlet
f = Figlet(font='slant')
print (f.renderText('\nO Bardo Ilusionista'))
#Tentar colocar cor depois /\
jogo_rapido_salvo = "x"
jogo_completo_salvo = "y"

p1 = []
p2 = []
p3 = []
p4 = []
p5 = []

print("\nModo de Jogo")
print("\n[1] Jogo Rápido (Seleciona entre personagens já criados e as batalhas são mais rápidas)")
print("[2] Jogo Completo (Cria o seu personagem e as batalhas são mais completas)")
print("[3] Sair do Jogo\n")

modo_de_jogo = ''
mre = ''

def modo_de_jogo(modo_escolhido):
    if int(modo_escolhido) == 1: #Jogo Rápido
        print("\n[1] Novo Jogo ")
        print("[2] Continuar \n")
        mre = input("Deseja começar um novo jogo ou continuar o seu jogo salvo? ")
        while mre not in {"1","2"}:
            print('')
            mre = input("Deseja começar um novo jogo ou continuar o seu jogo salvo? ")
        modo_rapido_escolhido(int(mre))
    elif int(modo_escolhido) == 2: #Jogo Completo
        print("\n[1] Novo Jogo ")
        print("[2] Continuar \n")

    elif int(modo_escolhido) == 3:
        print('')
        quit()

def modo_rapido_escolhido(jogador_ligeiro):
    if jogador_ligeiro == 1:
        jr.lista_de_personagens() #MEXER AQUI

    elif jogador_ligeiro == 2:
        print("\nAinda não há jogo salvo campeão!\n")


modo_escolhido = input("\nQual modo você deseja jogar? (1,2 ou 3) ")

while modo_escolhido not in {"1","2","3"}:
    modo_escolhido = input("\nQual modo você deseja jogar? (1,2 ou 3) ")

modo_de_jogo(int(modo_escolhido))