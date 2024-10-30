from Data import Data

class Competicao:
    def __init__(self, nome, data):
        self.__nome = nome
        self.__data = data


    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        return self.__nome


    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data: int):
        return self.__data
    
    def imprime_data(self):
        print("\nData da competição:\n")
        print(f"{self.__data}\n")

a1 = Competicao('Sol','20/10/2024')
a1.imprime_data

