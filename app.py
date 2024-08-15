"""
Módulo de Gerenciamento de Contatos

Este módulo implementa a aplicação de gerenciamento de contatos, proporcionando
um loop principal que permite ao usuário interagir com o sistema por meio de um menu.

O menu oferece opções para criar um novo contato, buscar um contato, editar, listar contatos existentes,
ou encerrar a aplicação.

Funções:
--------
app() -> None
    Executa o loop principal da aplicação de gerenciamento de contatos. Exibe
    um menu de opções para o usuário e aguarda a seleção, executando ações
    correspondentes com base na escolha.

Uso:
-----
    Para executar a aplicação, use o seguinte comando:

    python main.py

    O menu será exibido, permitindo ao usuário selecionar entre criar um novo
    contato, listar contatos, ou encerrar a aplicação.
"""

# python -m pip freeze > config/requirements.txt
# python -m pip install -r config/requirements.txt

from util.menu import menu
from database.db_initializer import initialize_database, create_tables
from database.db_operations import DBOperation
from factory.contact_creator import ContactCreator
from classes.contact import Contact
from database.db_connection import get_session
from util.logging_config import setup_logging

# Configurar o logging
setup_logging()


def initialize_system():
    """
    Inicializa o banco de dados e as tabelas.
    """
    initialize_database()
    create_tables()


def session():
    """
    Retorna uma nova sessão do banco de dados.

    Retorna:
        session (Session): Instância da sessão SQLAlchemy.
    """
    return get_session()


def create_contact():
    """
    Cria um novo contato e o salva no banco de dados.
    """
    contact = ContactCreator.get_instance_contact()
    DBOperation.save_obj_db(contact, session())
    print("Contato criado com sucesso!")


def list_contacts():
    """
    Lista todos os contatos armazenados no banco de dados.
    """
    contacts = DBOperation.find_objs_db(Contact, session())
    if contacts:
        for contact in contacts:
            print(contact)
    else:
        print("@@@ Nenhum contato cadastrado. @@@")


def handle_option(option):
    """
    Manipula a opção selecionada pelo usuário.
    """
    if option == "1":
        create_contact()
    elif option == "2":
        list_contacts()
    elif option == "0":
        print("Encerrando aplicação!")
        return True
    else:
        print("Opção inválida!")
    return False


def app():
    """
    Executa o loop principal da aplicação de gerenciamento de contatos.

    Exibe um menu de opções para o usuário e aguarda a seleção
    de uma das seguintes opções:

    - "1": Criação de um novo contato.
    - "2": Listagem de todos os contatos.
    - "0": Encerramento da aplicação.

    O loop continua até que a opção "0" seja selecionada.
    """

    initialize_system()

    while True:
        opcao = menu()

        if handle_option(option=opcao):
            break

        # get_session().close()


if __name__ == "__main__":
    app()
