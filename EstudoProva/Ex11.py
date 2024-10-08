# Classe Livro
class Livro:
    def __init__(self, titulo, autor, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.quantidade = quantidade

    def verificar_disponibilidade(self):
        """Verifica se há exemplares disponíveis"""
        return self.quantidade > 0

    def __str__(self):
        """Representação em formato de string do livro"""
        return f"{self.titulo}, {self.autor}, {self.quantidade}"


# Classe Biblioteca
class Biblioteca:
    def __init__(self, arquivo='livros.txt'):
        self.arquivo = arquivo
        self.livros = []
        self.carregar_livros()

    def criar_arquivo(self):
        """Cria o arquivo de livros se não existir"""
        with open(self.arquivo, 'a') as arquivo:
            pass
        print(f"Arquivo '{self.arquivo}' criado ou já existente.")

    def carregar_livros(self):
        """Carrega os livros do arquivo para a lista de livros"""
        try:
            with open(self.arquivo, 'r') as arquivo:
                for linha in arquivo:
                    titulo, autor, quantidade = linha.strip().split(', ')
                    self.livros.append(Livro(titulo, autor, int(quantidade)))
        except FileNotFoundError:
            self.criar_arquivo()

    def salvar_livros(self):
        """Salva os livros da lista de volta no arquivo"""
        with open(self.arquivo, 'w') as arquivo:
            for livro in self.livros:
                arquivo.write(f"{livro}\n")

    def adicionar_livro(self, titulo, autor, quantidade):
        """Adiciona um novo livro à biblioteca"""
        novo_livro = Livro(titulo, autor, quantidade)
        self.livros.append(novo_livro)
        self.salvar_livros()
        print(f"Livro '{titulo}' adicionado com sucesso!")

    def verificar_disponibilidade(self, titulo_procurado):
        """Verifica se o livro está disponível e se há exemplares"""
        for livro in self.livros:
            if livro.titulo.lower() == titulo_procurado.lower():
                if livro.verificar_disponibilidade():
                    print(f"O livro '{livro.titulo}' está disponível com {livro.quantidade} exemplares.")
                else:
                    print(f"O livro '{livro.titulo}' está esgotado.")
                return
        print(f"O livro '{titulo_procurado}' não está disponível na biblioteca.")

    def exibir_acervo(self):
        """Exibe todos os livros da biblioteca"""
        if not self.livros:
            print("Nenhum livro no acervo.")
        else:
            print("Acervo da Biblioteca:")
            for livro in self.livros:
                print(f"- {livro.titulo} de {livro.autor} ({livro.quantidade} exemplares)")


# Exemplo de uso das classes

# Inicializando a biblioteca e carregando livros do arquivo
biblioteca = Biblioteca()

# Adicionando livros à biblioteca
biblioteca.adicionar_livro("O Alquimista", "Paulo Coelho", 5)
biblioteca.adicionar_livro("1984", "George Orwell", 3)

# Verificando disponibilidade de livros
biblioteca.verificar_disponibilidade("O Alquimista")
biblioteca.verificar_disponibilidade("Harry Potter e a Pedra Filosofal")

# Exibindo o acervo completo
biblioteca.exibir_acervo()
