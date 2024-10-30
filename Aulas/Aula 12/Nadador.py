from Atleta import Atleta
class Nadador(Atleta):
    def __init__(self, nome, idade: int, categoria):
        super().__init__(nome,idade)
        self.__categoria = categoria

    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, categoria):
        return self.__categoria
    
    def imprime_info(self):
        super().imprime_info()
        print(f"Categoria: {self.__categoria}")



