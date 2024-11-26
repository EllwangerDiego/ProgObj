from Aluno import Aluno
from GrauA import GrauA
from GrauB import GrauB

class Turma():
    def __init__(self, codigo: str, lista_alunos = [], capacidade = 0):
        self._codigo = codigo
        self._lista_alunos = lista_alunos
        self._capacidade = capacidade
        

    def insere_aluno(self):
        if self._capacidade > 0:
            nome = input("Digite aqui o nome do aluno: ")
            self._ga = float(input("Digite aqui a nota do GA: "))
            self._gb = float(input("Digite aqui a nota do GB: "))
            aluno = Aluno(nome, self._ga, self._gb)

            self._lista_alunos.append(aluno)
            self._capacidade = self._capacidade - 1
        else:
            print("Capacidade maxima de alunos")

    def media_notas_turma(self):
        if len(self._lista_alunos) == 0:
            return -1
        
        soma_notas = 0

        for aluno in self._lista_alunos:
            final = (aluno.ga + (aluno.gb * 2))/3
            soma_notas = soma_notas + final

        media_turma = soma_notas /len(self._lista_alunos)
        return media_turma
    
    def altera_notas_ga(self):
        alunox = input("Digite aqui o nome do aluno para alterar a nota do GA: ")
        nota_trabalho = float(input("Digite aqui a nota do trabalho: "))
        nota_prova = float(input("Digite aqui a nota da prova: "))
        aluno = GrauA(nota_trabalho, nota_prova)
        aluno.calcula_nota_final_grau()

    def altera_notas_gb(self):
        nota_atividades = float(input("Digite aqui a nota das atividades: "))
        nota_seminario = float(input("Digite aqui a nota do seminario: "))
        nota_participacao = float(input("Digite aqui a nota de participacao: "))
        aluno = GrauB(nota_atividades, nota_seminario,nota_participacao)
        aluno.calcula_nota_final_grau()


    def lista_alunos(self):
        print("Lista de Alunos:")
        for aluno in self._lista_alunos:
            print(f"Nome: {aluno.nome}")
        
turma = Turma('Turma A')
turma.insere_aluno()
turma.lista_alunos()
print("Media das notas da turma: ",turma.media_notas_turma())
