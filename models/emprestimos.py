from utils.logger import registrar_log

def registrar_emprestimo(cursor, conexao, id_usuario, id_livro):
    query = """
    INSERT INTO emprestimos (id_usuario, id_livro, data_emprestimo)
    VALUES (%s, %s, CURRENT_DATE);
    UPDATE livros
    SET disponivel = FALSE
    WHERE id = %s;
    """
    cursor.execute(query, (id_usuario, id_livro, id_livro))
    conexao.commit()
    mensagem = f"Empréstimo registrado: Usuário {id_usuario} emprestou o livro {id_livro}."
    print(mensagem)
    registrar_log(mensagem)

def registrar_devolucao(cursor, conexao, id_livro):
    query = """
    UPDATE emprestimos
    SET data_devolucao = CURRENT_DATE
    WHERE id_livro = %s AND data_devolucao IS NULL;
    UPDATE livros
    SET disponivel = TRUE
    WHERE id = %s;
    """
    cursor.execute(query, (id_livro, id_livro))
    conexao.commit()
    mensagem = f"Devolução registrada: Livro {id_livro} está disponível novamente."
    print(mensagem)
    registrar_log(mensagem)
