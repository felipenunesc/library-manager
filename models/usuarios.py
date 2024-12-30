from utils.logger import registrar_log

def cadastrar_usuario(cursor, conexao, nome):
    query = """
    INSERT INTO usuarios (nome, historico)
    VALUES (%s, NULL);
    """
    cursor.execute(query, (nome,))
    conexao.commit()
    mensagem = f"Usuário '{nome}' cadastrado com sucesso!"
    print(mensagem)
    registrar_log(mensagem)
    

def buscar_usuario_por_id(cursor, id):
    query = """
    SELECT id, nome, historico
    FROM usuarios
    WHERE id = %s;
    """
    cursor.execute(query, (id,))
    usuario = cursor.fetchone()
    if usuario:
        print(f"ID: {usuario[0]} | Nome: {usuario[1]} | Histórico: {usuario[2]}")
    else:
        print("Usuário não encontrado.")
