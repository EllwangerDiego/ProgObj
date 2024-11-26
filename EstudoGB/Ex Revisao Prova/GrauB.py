from Grau import Grau
class GrauB(Grau):
    def __init__(self, nota_atividades, nota_seminario, nota_participacao):
        self._nota_atividades = nota_atividades
        self._nota_seminario = nota_seminario
        self._nota_participacao = nota_participacao

    @property
    def nota_atividades(self):
        return self._nota_atividades
    
    @nota_atividades.setter
    def nota_atividades(self, nota_atividades):
        self._nota_atividades = nota_atividades

    @property
    def nota_seminario(self):
        return self._nota_seminario
    
    @nota_seminario.setter
    def nota_seminario(self, nota_seminario):
        self._nota_seminario = nota_seminario

    @property
    def nota_participacao(self):
        return self._nota_participacao
    
    @nota_seminario.setter
    def nota_participacao(self, nota_participacao):
        self._nota_participacao = nota_participacao

    def __str__(self):
        return f"Nota Atividades: {self._nota_atividades}\nNota Seminario: {self.nota_seminario}\nNota Participacao: {self._nota_participacao}"
    
    def imprime_info(self):
        print(f"Nota Atividades: {self._nota_atividades}\nNota Seminario: {self.nota_seminario}\nNota Participacao: {self._nota_participacao}")

    def calcula_nota_final_grau(self):
        atividades = self._nota_atividades * 0.30
        seminario = self._nota_seminario * 0.60
        participacao = self._nota_participacao * 0.10
        final = atividades + seminario + participacao
        print(f"Nota final: {final}")

Diego = GrauB(10,9,8)
Diego.imprime_info()
Diego.calcula_nota_final_grau()