from typing import Type

class Interruptor:
    def __init___(self, comodo: str):
        self.__comodo = comodo

    def acender(self):
        print(f'Acendendo {self.__comodo}')

    def apagar(self):
        print(f'Apagando {self.__comodo}')

class Pessoa:
    def acender_luz(self, interruptor: Type[Interruptor]):
        interruptor.acender()

    def apagar_luz(self, interruptor: Type[Interruptor]):
        interruptor.apagar()
    
    def dormir(self):
        print('Fui dormir...')
        

lhama = Pessoa()
interruptor_quarto = Interruptor('quarto')

interruptor_quarto.acender()
lhama.acender_luz(interruptor_quarto)
