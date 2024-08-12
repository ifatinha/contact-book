"""
Módulo de Inicialização do Banco de Dados

Este módulo contém funções para verificar e criar o banco de dados necessário
para a aplicação de gerenciamento de contatos.
"""

from database.db_create import DBCreate

# Variável global para rastrear se o banco de dados já foi criado
DATABASE_INITIALIZED = False


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
