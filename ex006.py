import random

class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def latir(self):
        print(f"{self.nome} está latindo: Au au!")

    def comer(self):
        print(f"{self.nome} está comendo")

cachorros = []
nomes = ["Rex", "Bello", "Toby"]
racas = ["Labrador", "Golden Retriever", "Poodle"]

nomes.sort()

for i in range(len(racas)):
    cachorros.append(Cachorro(nomes[i], racas[i], random.randint(1, 15)))

for cachorro in cachorros:
    print(f"Nome: {cachorro.nome}, Raça: {cachorro.raca}, Idade: {cachorro.idade}")
    cachorro.latir()
    cachorro.comer()