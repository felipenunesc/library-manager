from utils.logger import registrar_log

def cadastrar_livro(cursor, conexao, titulo, autor, ano):
    query = """
    INSERT INTO livros (titulo, autor, ano, disponivel)
    VALUES (%s, %s, %s, TRUE);
    """
    cursor.execute(query, (titulo, autor, ano))
    conexao.commit()
    mensagem = f"Livro '{titulo}' cadastrado com sucesso!"
    print(mensagem)
    registrar_log(mensagem)

def listar_livros_disponiveis(cursor):
    query = """
    SELECT id, titulo, autor, ano
    FROM livros
    WHERE disponivel = TRUE;
    """
    cursor.execute(query)
    livros = cursor.fetchall()
    print("Livros Disponíveis:")
    for livro in livros:
        print(f"ID: {livro[0]} | Título: {livro[1]} | Autor: {livro[2]} | Ano: {livro[3]}")
