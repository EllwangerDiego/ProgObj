class Livro:
    def __init__(self, titulo, autor, exemplares):
        self.titulo = titulo
        self.autor = autor
        self.exemplares_disponiveis = exemplares
        self.exemplares_emprestados = 0

    def emprestar(self):
        if self.exemplares_disponiveis > 0:
            self.exemplares_disponiveis -= 1
            self.exemplares_emprestados += 1
            print(f"Livro '{self.titulo}' emprestado com sucesso!")
        else:
            print(f"Livro '{self.titulo}' não disponível para empréstimo!")

    def devolver(self):
        if self.exemplares_emprestados > 0:
            self.exemplares_disponiveis += 1
            self.exemplares_emprestados += -1
            print(f"Livro '{self.titulo}' devolvido com sucesso!")
        else:
            print(f"Nenhum exemplar de '{self.titulo}' está emprestado!")

    def reservar(self):
        if self.exemplares_disponiveis == 0:
            print(f"Livro '{self.titulo}' reservado com sucesso!")
        else:
            print(f"Livro '{self.titulo}' está disponível, não é necessário reservar.")


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

    def solicitar_emprestimo(self, livro):
        if len(self.livros_emprestados) >= 5:
            print(f"{self.nome} já possui 5 livros emprestados.")
            return
        livro.emprestar()
        if livro.exemplares_emprestados > 0:
            self.livros_emprestados.append(livro)

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            livro.devolver()
            self.livros_emprestados.remove(livro)
        else:
            print(f"{self.nome} não tem o livro '{livro.titulo}' para devolver.")

    def reservar_livro(self, livro):
        livro.reservar()

    def listar_livros_emprestados(self):
        if self.livros_emprestados:
            print(f"Livros emprestados por {self.nome}:")
            for livro in self.livros_emprestados:
                print(f" - {livro.titulo}")
        else:
            print(f"{self.nome} não possui livros emprestados.")


class Biblioteca:
    def __init__(self):
        self.acervo = []

    def cadastrar_livro(self, titulo, autor, exemplares):
        livro = Livro(titulo, autor, exemplares)
        self.acervo.append(livro)
        print(f"Livro '{titulo}' cadastrado com sucesso.")

    def remover_livro(self, titulo):
        livro = self.buscar_livro(titulo)
        if livro:
            self.acervo.remove(livro)
            print(f"Livro '{titulo}' removido do acervo.")
        else:
            print(f"Livro '{titulo}' não encontrado no acervo.")

    def consultar_livros(self):
        print("Livros disponíveis no acervo:")
        for livro in self.acervo:
            print(f" - {livro.titulo} ({livro.exemplares_disponiveis} disponíveis)")

    def buscar_livro(self, titulo):
        for livro in self.acervo:
            if livro.titulo == titulo:
                return livro
        return None

    def gerar_relatorio_acervo(self):
        print("Relatório de acervo:")
        for livro in self.acervo:
            print(f"Livro: {livro.titulo}, Disponíveis: {livro.exemplares_disponiveis}, Emprestados: {livro.exemplares_emprestados}")

    def gerar_relatorio_emprestimos_usuario(self, usuario):
        usuario.listar_livros_emprestados()


# Exemplo de uso
biblioteca = Biblioteca()

# Cadastrar livros no acervo
biblioteca.cadastrar_livro("Python para Todos", "Al Sweigart", 3)
biblioteca.cadastrar_livro("O Senhor dos Anéis", "J.R.R. Tolkien", 5)

# Criar usuário
usuario = Usuario("João")

# Consultar livros disponíveis
biblioteca.consultar_livros()

# Solicitar empréstimo
livro = biblioteca.buscar_livro("Python para Todos")
usuario.solicitar_emprestimo(livro)

# Gerar relatório de acervo
biblioteca.gerar_relatorio_acervo()

# Gerar relatório de empréstimos de um usuário
biblioteca.gerar_relatorio_emprestimos_usuario(usuario)

# Devolver livro
usuario.devolver_livro(livro)

# Gerar relatório novamente após devolução
biblioteca.gerar_relatorio_acervo()
