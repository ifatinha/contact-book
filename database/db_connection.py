"""
db_connection.py

Este módulo gerencia a conexão com o banco de dados MySQL utilizando o SQLAlchemy.

Funções:
- init_db(): Inicializa a conexão com o banco de dados e retorna o engine e a base declarativa.
- get_session(): Retorna uma nova sessão de conexão com o banco de dados.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from database.config import get_database_url

# Inicializa a conexão com o banco de dados


def init_db():
    """
    Inicializa o engine e a base declarativa do SQLAlchemy.

    Returns:
        tuple: Contendo o engine do SQLAlchemy e a classe base declarativa.
    """

    engine_temp = create_engine(get_database_url(), echo=True)
    base_temp = declarative_base()
    return engine_temp, base_temp


# Criação da engine e da base
engine, Base = init_db()

# Criação da fabrica de sessões
Session = sessionmaker(bind=engine)


def get_session():
    """
    Retorna uma nova sessão de conexão com o banco de dados.

    Returns:
        Session: Uma nova instância de sessão para interagir com o banco de dados.
    """
    return Session()
