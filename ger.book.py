#criei uma classe de livros para separar por nomes, autor,ano e editora
class Livros:
    def __init__(self, nome,genero, autor, ano, editora):
        self.nome = nome
        self.autor = autor
        self.ano = ano
        self.editora = editora
        self.genero = genero

lista_livros = []

def cadastrar_livro():
    nome = input('Informe o nome do livro: ')
    genero =input('Informe o gênero do livro:')
    autor = input('Informe o autor: ')
    ano = int(input('Informe o ano: '))
    editora = input('Informe a editora: ')
    print('Livro Cadastrado com sucesso!')

    livro = Livros(nome,genero, autor, ano, editora)
    lista_livros.append(livro)
    return livro

def listar_livros():
    for livro in lista_livros:
        print("Nome:", livro.nome)
        print('Gênero:',livro.genero)
        print("Autor:", livro.autor)
        print("Ano:", livro.ano)
        print("Editora:", livro.editora)
        print()

def main():
    while True:
        opcao = input('Escolha a opção:\n1-Cadastrar Livro\n2-Listar livros\n3-Sair\n')

        if opcao == '1':
            cadastrar_livro()
        elif opcao == '2':
            listar_livros()
        elif opcao == '3':
            break
        else:
            print('Opção Inválida!')

if __name__ == '__main__':
    main()
