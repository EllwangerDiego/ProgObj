class Aluno():
    def __init__(self, nome, ga: 0, gb: 0):
        self._nome = nome
        self._ga = ga
        self._gb = gb
        

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def ga(self):
        return self._ga
    
    @ga.setter
    def ga(self,ga):
        self._ga = ga

    @property
    def gb(self):
        return self._gb
    
    @gb.setter
    def gb(self,gb):
        self._gb = gb

    def calcula_nota_final(self):
        nota_final = (self._ga + (self._gb * 2))/3
        print(f"Nota Final: {nota_final}")

