from Grau import Grau
class GrauA(Grau):
    def __init__(self, nota_trabalho: float, nota_prova: float):
        self._nota_trabalho = nota_trabalho
        self._nota_prova = nota_prova

    @property
    def nota_trabalho(self):
        return self._nota_trabalho
    
    @nota_trabalho.setter
    def nota_trabalho(self, nota_trabalho):
        self._nota_trabalho = nota_trabalho

    @property
    def nota_prova(self):
        return self._nota_prova
    
    @nota_prova.setter
    def nota_prova(self, nota_prova):
        self._nota_prova = nota_prova

    def __str__(self):
        return f"{self._nota_trabalho}{self._nota_prova}"
    
    def imprime_info(self):
        print(f"Nota trabalho: {self._nota_trabalho}\nNota Prova: {self._nota_prova}\n")
        


    def calcula_nota_final_grau(self):
        trabalho = self._nota_trabalho * 0.30
        prova = self._nota_prova * 0.70
        final = trabalho + prova
        print(f"Nota final: {final}")

    
Notas = GrauA(10, 9)
Notas.imprime_info()
Notas.calcula_nota_final_grau()