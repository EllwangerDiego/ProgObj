class Livro:
    def __init__(self, titulo):
        self.titulo = titulo

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca '{self.nome}'.")

# Criando livros
livro1 = Livro("Python Básico")
livro2 = Livro("Estruturas de Dados")

# Criando biblioteca e agregando livros
biblioteca = Biblioteca("Biblioteca Central")
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
