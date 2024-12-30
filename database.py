import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def conectar_banco():
    """
    Estabelece conexão com o banco de dados PostgreSQL.

    Returns:
        conexao: Objeto de conexão ao banco.
        cursor: Cursor para executar consultas SQL.
    """
    try:
        conexao = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        cursor = conexao.cursor()
        print("Conexão ao banco de dados estabelecida com sucesso.")
        return conexao, cursor
    except Exception as e:
        print("Erro ao conectar ao banco de dados:", e)
        raise