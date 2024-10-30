from Atleta import Atleta
from Competicao import Competicao
class Corredor(Atleta):
    def __init__(self, nome, idade: int, peso):
        super().__init__(nome,idade)
        self.__peso = peso

    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self, peso):
        return self.__peso
    
    def imprime_info(self):
        super().imprime_info()
        print(f"Peso {self.__peso}")
    
    def imprime_competicao(self):
        print("Categoria tipo: Corredor")

