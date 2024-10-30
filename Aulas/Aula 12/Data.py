class Data:
    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, dia):
        self.__nome = dia

    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self,mes):
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self,ano):
        self.__ano = ano


    def recebe_data(self):
        self.__dia = int(input("Informe o dia do evento: "))
        self.__mes = int(input("Informe o mês do evento: "))
        self.__ano = int(input("Informe o ano do evento: "))

    def imprime_data(self):
        print("\nData da Competição:\n")
        print(f"{self.__dia}/{self.__mes}/{self.__ano}\n")

a1 = Data(29,10,2024)
a1.imprime_data()



