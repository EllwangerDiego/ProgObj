from veiculo import Veiculo

class Terrestre(Veiculo):
    def __init__(self, ano: int, peso: int, tanque: float, modelo: str, qtRoda: int, qtPorta: int):
        super().__init__(ano, peso, tanque, modelo)
        self.__qtRoda = qtRoda
        self.__qtPorta = qtPorta

    @property
    def qtRoda(self) -> int:
        return self.__qtRoda

    @qtRoda.setter
    def qtRoda(self, qtRoda: int) -> None:
        self.__qtRoda = qtRoda

    @property
    def qtPorta(self) -> int:
        return self.__qtPorta

    @qtPorta.setter
    def qtPorta(self, qtPorta: int) -> None:
        return self.__qtPorta

    def consumo(self) -> float:
        return 1 / ((super().peso * 0.00005) + (self.qtRoda * 0.005))

    def autonomia(self) -> float:
        return self.consumo() * super().tanque

    def info(self) -> None:
        super().info()
        print(f"Qtde rodas: {qtRoda}\n Qtde portas: {qtPorta}\nConsumo: {self.consumo()}\nAutonomia: {self.autonomia()}")
