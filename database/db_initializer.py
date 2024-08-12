"""
Módulo de Inicialização do Banco de Dados

Este módulo contém funções para inicializar o banco de dados necessário
para a aplicação de gerenciamento de contatos. Ele inclui a verificação da
existência do banco de dados e a criação das tabelas se necessário.
"""

from database.db_create import DBCreate
from database.db_connection import engine, Base

# Variável global para rastrear se o banco de dados já foi criado
DATABASE_INITIALIZED = False
TABLE_INITIALIZED = False


def initialize_database() -> None:
    """
    Inicializa o banco de dados se ainda não tiver sido inicializado.

    Esta função verifica se o banco de dados já foi criado, e se não,
    executa o processo de criação do banco de dados.
    """

    global DATABASE_INITIALIZED

    if not DATABASE_INITIALIZED:
        DBCreate.check_and_create_database("contact-book")
        DATABASE_INITIALIZED = True


def create_tables() -> None:
    """
    Cria todas as tabelas do banco de dados se ainda não existirem.

    Esta função utiliza a metadata do SQLAlchemy para criar todas as tabelas
    definidas nos modelos do banco de dados, se elas ainda não existirem.

    :return: None
    """

    global TABLE_INITIALIZED

    if not TABLE_INITIALIZED:
        Base.metadata.create_all(engine)
        TABLE_INITIALIZED = True
