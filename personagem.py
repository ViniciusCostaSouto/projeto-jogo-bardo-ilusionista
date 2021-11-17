class Personagem_Rapido():
    def __init__(self, nome, raça, classe):
        self.nome = nome
        self.raça = raça
        self.classe = classe

if __name__ == "__main__":
    personagem1 = Personagem_Rapido("Cleiton", "Humano", "Cuzão")
    print(personagem1.nome)
    print(personagem1.raça)
    print(personagem1.classe)