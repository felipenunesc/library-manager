from database import conectar_banco
from utils.menu import exibir_menu
from models.livros import *
from models.usuarios import *
from models.emprestimos import *
import os

def main():
    conexao, cursor = conectar_banco()
    
    if not os.path.exists("logs"):
        os.makedirs("logs")
    
    while True:
        opcao = exibir_menu()
        
        if opcao == 1:
            listar_livros_disponiveis(cursor)
        elif opcao == 2:
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            ano = int(input("Ano de publicação: "))
            cadastrar_livro(cursor, conexao, titulo, autor, ano)
        elif opcao == 3:
            nome = input("Nome do usuário: ")
            cadastrar_usuario(cursor, conexao, nome)
        elif opcao == 4:
            id_usuario = int(input("ID do usuário: "))
            id_livro = int(input("ID do livro: "))
            registrar_emprestimo(cursor, conexao, id_usuario, id_livro)
        elif opcao == 5:
            id_livro = int(input("ID do livro: "))
            registrar_devolucao(cursor, conexao, id_livro)
        elif opcao == 6:
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida, tente novamente.")

    cursor.close()
    conexao.close()

if __name__ == "__main__":
    main()
