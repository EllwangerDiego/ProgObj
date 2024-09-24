class Teste():
    def __init__(self, valor):
        self.x = valor

    def get_valor(self):
        '''Metodo getter para retornar o valor do atributo x:'''
        return self.x
    
    def set_valor(self, v):
        '''Metodo Setter para atribuir novo valor ao atributo x'''
        self.x = v

teste = Teste(10)
print('Valor do objeto: ', teste.get_valor())

val = int(input("Digite um valor: "))
teste.set_valor(val)
print('Valor do objeto apos: ', teste.get_valor())

