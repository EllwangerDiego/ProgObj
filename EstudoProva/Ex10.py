def criar_arquivo():
    # O modo 'a' (append) cria o arquivo caso ele não exista, mas não sobrescreve se já existir.
    with open('livros.txt', 'a') as arquivo:
        pass  # Usamos 'pass' porque não precisamos escrever nada no momento
    print("Arquivo 'livros.txt' criado ou já existente.")

criar_arquivo()