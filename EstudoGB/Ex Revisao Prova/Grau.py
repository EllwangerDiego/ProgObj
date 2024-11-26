class Grau():
    def __init__(self, data_comeco, data_fim):
        self._data_comeco = data_comeco
        self._data_fim = data_fim

    @property
    def data_comeco(self):
        return self._data_comeco
    
    @data_comeco.setter
    def data_comeco(self,data_comeco):
        self._data_comeco = data_comeco

    @property
    def data_fim(self):
        return self._data_fim
    
    @data_fim.setter
    def data_fim(self,data_fim):
        self._data_fim = data_fim

    def __str__(self):
        return f"{self.data_comeco}{self.data_fim}"
    
GrauA = Grau('06/02/2006', '26/11/2024')
