class Exemplo:
    def __init__(self):
        self.atributo_publico = 10          # Público
        self._atributo_protegido = 5        # Protegido
        self.__atributo_privado = 42        # Privado
    
    # Método público
    def metodo_publico(self):
        print(f"Atributo público: {self.atributo_publico}")
        self.__metodo_privado()  # Acesso a método privado dentro da própria classe

    # Método protegido
    def _metodo_protegido(self):
        print(f"Atributo protegido: {self._atributo_protegido}")

    # Método privado
    def __metodo_privado(self):
        print(f"Atributo privado: {self.__atributo_privado}")


# Exemplo de uso
exemplo = Exemplo()

# Acessando atributo e método públicos
print(exemplo.atributo_publico)
exemplo.metodo_publico()

# Acessando atributo e método protegidos (não recomendado diretamente)
print(exemplo._atributo_protegido)
exemplo._metodo_protegido()

# Tentativa de acesso ao atributo e método privados - isso vai falhar
try:
    print(exemplo.__atributo_privado)  # Gera AttributeError
except AttributeError as e:
    print(f"Erro: {e}")

# Tentativa de chamar método privado diretamente - também falha
try:
    exemplo.__metodo_privado()  # Gera AttributeError
except AttributeError as e:
    print(f"Erro: {e}")

# Acesso por 'name mangling' (não recomendado)
print(exemplo._Exemplo__atributo_privado)  # Funciona, mas não deve ser usado
