"""
Configurações de Conexão com o Banco de Dados MySQL.

Este arquivo contém as credenciais para conectar-se ao banco de dados usado na aplicação.

Funções:
- get_database_url(): Retorna a URL de conexão no formato necessário para o SQLAlchemy,
  utilizando as credenciais e informações de conexão definidas no dicionário DATABASE_CONFIG.

Variáveis:
- DATABASE_CONFIG: Dicionário contendo as informações de configuração do banco de dados,
  como usuário, senha, host e nome do banco de dados.

Aviso:
    Mantenha este arquivo seguro e evite compartilhá-lo publicamente,
    pois ele contém informações sensíveis que podem comprometer a segurança da aplicação.

"""

DATABASE_CONFIG = {
    "user": "root",
    # "password": "admin",
    "password": "12345",
    "host": "127.0.0.1",
    "database": "contact-book"
}


def get_database_url():
    """
    Gera a URL de conexão para o banco de dados MySQL.

    Returns:
        str: URL de conexão formatada para ser usada pelo SQLAlchemy.
    """

    return f"mysql+pymysql://{DATABASE_CONFIG['user']}:{DATABASE_CONFIG['password']}@"\
        f"{DATABASE_CONFIG['host']}/{DATABASE_CONFIG['database']}"
