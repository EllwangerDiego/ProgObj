import random
from Aluno import Aluno
from Grau import Grau
from GrauA import GrauA
from GrauB import GrauB
from Turma import Turma



def main():
    codigo = int(input("Digite aqui o codigo da turma: "))
    capacidade = random.randint(1,100)
    
    Turma(codigo,'',capacidade)

main()