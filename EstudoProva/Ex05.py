class Humano:
    

    def __init__(self, nome: str, idade: int) -> None:
        
        self.nome = nome
        self.idade = idade
    
    def falar(self, algo: str) -> str:

        return f'falando sobre {algo} ...'
    
    def ligar(self, contato: str) -> None:

        msg = f'Ligando para {contato} ...'
        print(msg)

    def comprar(self, produto: str, loja: str) -> None:

        msg = f"Comprando {produto} em {loja} ..."
        print(msg)

jarvis = Humano("Edwing Jarvis", 35)

class Ultron(Humano):
    pass
