"""
    Classe de teste
"""

from database.db_create import DBCreate
DBCreate.check_and_create_database("contact-book")

# from database.db_connection import engine, Base

# Criando todas as tabelas do banco de dados (se elas ainda nao existirem)
# Base.metadata.create_all(engine)

# Usando a sessão para interagir com o banco de dados
# session = get_session()
