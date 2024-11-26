from Ex1 import Atleta
class Nadador(Atleta):
    def __init__(self, nome, idade, categoria):
        super().__init__(nome, idade)
        self.categoria = categoria

    def imprime_info(self):
        super().imprime_info()
        print(f'Categoria: {self.categoria}')

Jorge = Nadador('Jorge', '19', 'Bronze')
Jorge.imprime_info()