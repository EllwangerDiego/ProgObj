class Atleta:
    def __init__(self, nome, idade: int):
        self.__nome = nome
        self.__idade = idade

    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        return self.__nome


    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade: int):
        return self.__nome

    def imprime_info(self):
        print("\nInformações do Atleta:")
        print(f"Nome: {self.__nome}\nIdade: {self.__idade}\n")


a1= Atleta('pedro',18)

a1.imprime_info()
    


