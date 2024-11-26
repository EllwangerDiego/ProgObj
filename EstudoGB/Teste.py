class Mae:
    def __init__(self, endereco, sobrenome):
        self.endereco = endereco
        self.sobrenome = sobrenome

    def comer(self):
        print('Estou comendo')

    def estudar(self):
        print(f'Estou Estudando')

class Filha(Mae):
    def __init__(self, endereco, sobrenome):
        super().__init__(endereco, sobrenome)
        
    def brincar(self, brinquedo):
        print(f'estou brincando com {brinquedo}')


ana = Mae('Rua Elvira', 'Silva')
clara = Filha('Rua do Bolo', 'Jorge')
clara.brincar('boneca')

print(ana.endereco)
print(clara.endereco)
print(clara.sobrenome)
clara.estudar()