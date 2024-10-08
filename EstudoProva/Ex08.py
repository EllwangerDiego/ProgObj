class Aluno:
    def __init__(self, nome):
        self.nome = nome

class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
        print(f"Aluno {aluno.nome} adicionado à escola {self.nome}.")

# Criando instâncias de Aluno e Escola
escola = Escola("Escola Estadual")
aluno1 = Aluno("João")
aluno2 = Aluno("Maria")

# Associando os alunos à escola
escola.adicionar_aluno(aluno1)
escola.adicionar_aluno(aluno2)
