from datetime import datetime

def registrar_log(mensagem):
    """
    Registra uma mensagem no arquivo de log com a data e hora atual.

    Args:
        mensagem (str): Mensagem a ser registrada.
    """
    try:
        with open("logs/operacoes.log", "a") as log_file:
            data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(f"[{data_hora}] {mensagem}\n")
    except Exception as e:
        print(f"Erro ao registrar log: {e}")
