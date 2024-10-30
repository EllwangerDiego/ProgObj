from veiculo import Veiculo

class Aereo(Veiculo):
    def __init__(self, ano: int, peso: int, tanque: float, modelo: str, qtAsa: int, qtMotor: int):
        super().__init__(ano, peso, tanque, modelo)
        self.__qtAsa = qtAsa
        self.__qtMotor = qtMotor

    @property
    def qtAsa(self) -> int:
        return self.__qtAsa

    @qtAsa.setter
    def qtAsa(self, qtAsa: int) -> None:
        self.__qtAsa = qtAsa

    @property
    def qtMotor(self) -> int:
        return self.__qtMotor

    @qtMotor.setter
    def qtMotor(self, qtMotor: int) -> None:
        return self.__qtMotor

    def consumo(self) -> float:
        return 1 / ((super().peso * 0.00003) + (self.qtMotor * 0.01))

    def autonomia(self) -> float:
        return self.consumo() * super().tanque

    def info(self) -> None:
        super().info()
        print(f"Qt asas: {qtAsa}\n Qt motor: {qtMotor}\nConsumo: {self.consumo()}\nAutonmia: {self.autonomia()}")        
