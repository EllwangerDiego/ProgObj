from Ex2 import Data
class Competicao:
    def __init__(self, nome, data):  # A data agora é passada como parâmetro
        self.nome = nome
        self.data = data  # Atributo data, que é um objeto da classe Data

    def imprime_info(self):
        self.data.imprime_data()  # Chama o método da classe Data
        print(f'Nome da competição: {self.nome}')


# Criando a instância de Data (para a data da competição)
data_competicao = Data(15, 4, 2024)  # Data da competição

# Criando a instância de Competicao com nome e a data
competicao1 = Competicao("Maratona de São Paulo", data_competicao)  # Competição

# Chamando o método para imprimir as informações da competição
competicao1.imprime_info()

