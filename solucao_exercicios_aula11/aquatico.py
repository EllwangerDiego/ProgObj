from veiculo import Veiculo

class Aquatico(Veiculo):
    def __init__(self, ano: int, peso: int, tanque: float, modelo: str, qtMotor: int, qtConves: int):
        super().__init__(ano, peso, tanque, modelo)
        self.__qtMotor = qtMotor
        self.__qtConves = qtConves

    @property
    def qtMotor(self) -> int:
        return self.__qtMotor

    @qtMotor.setter
    def qtMotor(self, qtMotor: int) -> None:
        return self.__qtMotor
    @property
    def qtConves(self) -> int:
        return self.__qtConves

    @qtConves.setter
    def qtConves(self, qtConves: int) -> None:
        self.__qtConves = qtConves

    def consumo(self) -> float:
        return 1 / ((super().peso * 0.00002) + (self.qtMotor * 0.02))

    def autonomia(self) -> float:
        return self.consumo() * super().tanque

    def info(self) -> None:
        super().info()
        print(f"Qt motor: {qtMotor}\nQt convés: {qtConves}\nConsumo: {self.consumo()}\nAutonomia: {self.autonomia()}")        
