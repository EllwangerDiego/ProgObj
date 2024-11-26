from Ex1 import Atleta
from Ex2 import Data
from Ex3 import Competicao
class Corredor(Atleta):
    def __init__(self, nome, idade, peso, competicao):
        super().__init__(nome, idade)
        self.peso = peso
        self.competicao = competicao

    def imprime_competicao(self):
        print(f"Competição: {self.competicao.nome}")
        self.competicao.imprime_info()

    def imprime_info(self):
        super().imprime_info()
        print(f"Peso: {self.peso} kg")
        self.imprime_competicao()


# Criando objetos e testando o programa
data_competicao = Data(15, 4, 2024)  # Data da competição
competicao1 = Competicao("Maratona de São Paulo", data_competicao)  # Competição

corredor1 = Corredor("Cleber", 20, 70, competicao1)  # Corredor
corredor1.imprime_info()  # Imprime informações do corredor e da competição

