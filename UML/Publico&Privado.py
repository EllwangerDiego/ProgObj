#Publico
class MinhaClasse:
    def __init__(self):
        self.atributo_publico = "Eu sou público"

obj = MinhaClasse()
print(obj.atributo_publico)  # Acesso direto permitido


#Privado
class MinhaClasse:
    def __init__(self):
        self.__atributo_privado = "Eu sou privado"

    def __metodo_privado(self):
        return "Método privado"

obj = MinhaClasse()
# print(obj.__atributo_privado)  # Isso vai gerar um erro
print(obj._MinhaClasse__atributo_privado)  # Acesso permitido via name mangling


#Protegido
class MinhaClasse:
    def __init__(self):
        self._atributo_protegido = "Eu sou protegido"

obj = MinhaClasse()
print(obj._atributo_protegido)  # Acesso permitido, mas não recomendado
