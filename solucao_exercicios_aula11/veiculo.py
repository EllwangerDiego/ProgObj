class Veiculo:
    def __init__(self, ano: int, peso: float, tanque: float, modelo: str) -> None:
        self.__ano = ano
        self.__peso = peso
        self.__tanque = tanque
        self.__modelo = modelo

    @property
    def ano(self) -> int:
        return self.__ano

    @ano.setter
    def ano(self, ano: int) -> None:
        self.__ano = ano

    @property
    def peso(self) -> float:
        return self.__peso

    @peso.setter
    def peso(self, peso: float) -> None:
        self.__peso = peso

    @property
    def tanque(self) -> float:
        return self.__tanque

    @tanque.setter
    def tanque(self, tanque: float) -> None:
        self.__tanque = tanque

    @property
    def modelo(self) -> str:
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo: str) -> None:
        self.__modelo = modelo

    def consumo(self) -> float:
        pass

    def autonomia(self) -> float:
        pass

    def info(self) -> None:
        print("==== Informações do veículo ====")
        print(f"Ano: {ano}\nPeso: {peso}kg\nTanque: {tanque}L\nModelo: {modelo}")
