"""
Módulo para operações básicas de banco de dados usando SQLAlchemy.

Este módulo fornece a classe `DBOperation` para gerenciar transações no banco de dados,
incluindo operações de criação de esquema e inserção de dados.

Classes:
    DBOperation: Classe que fornece métodos estáticos para interagir com o banco de dados.

Métodos Estáticos:
    session: Cria e retorna uma nova sessão do banco de dados.
    object_save_db: Adiciona um objeto à base de dados e realiza commit.

Exceções:
    Captura e trata exceções relacionadas ao SQLAlchemy, incluindo `IntegrityError`,
    `OperationalError`, e `SQLAlchemyError`.

Uso:
    - `DBOperation.session()`: Cria e retorna uma nova sessão para interagir com o banco de dados.
    - `DBOperation.object_save_db(obj)`: Adiciona o objeto especificado ao banco de dados
       e faz commit, tratando exceções em caso de erro.

Exemplo:
    # Criar o esquema
    DBOperation.create_schema()

    # Adicionar um novo contato
    novo_contato = Contact(name="João Silva")
    DBOperation.object_save_db(novo_contato)
"""

from sqlalchemy.exc import SQLAlchemyError, IntegrityError, OperationalError


class DBOperation():

    """
    Classe para operações básicas de banco de dados usando SQLAlchemy.

    Métodos Estáticos:
        session: Cria e retorna uma nova sessão do banco de dados.
        save_contact: Adiciona um contato à base de dados e faz commit.
        find_contacts: Recupera todos os contatos do banco de dados.
        find_contact: Recupera um contato do banco de dados fazendo a consulta pelo nome.
        update_contact: Atualiza os dados de um contao.
        delete_contact: Deleta um contato.
    """

    @staticmethod
    def save_contact(obj, session):
        """
        Adiciona um objeto à base de dados e faz commit.

        Parâmetros:
            obj (Base): Instância do objeto a ser adicionado,
            que deve ser uma subclasse de `Base` do SQLAlchemy.

        Exceções:
            Rollback e exibição de mensagem de erro em caso de falha ao adicionar o objeto.

        Mensagens:
            Exibe uma mensagem de sucesso se o objeto for adicionado com sucesso ou uma mensagem
            de erro em caso de falha.
        """
        try:
            session.add(obj)
            session.commit()
            print(f"{obj.__class__.__name__} cadastrado com sucesso!")
        except IntegrityError as e:
            session.rollback()
            print(f"Erro de integridade ao adicionar classe: {e}")
        except OperationalError as e:
            session.rollback()
            print(f"Erro operacional ao adicionar classe: {e}")
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Erro SQLAlchemy ao adicionar classe: {e}")

    @staticmethod
    def find_contacts(Contact, session):
        """
        Busca todos os contatos do banco de dados.

        Parâmetros:
            Contact (Base): Classe a ser consultado,
            que deve ser uma subclasse de `Base` do SQLAlchemy.

        Retorna:
            list: Lista de instâncias de Contacts consultado.

        Exceções:
            Rollback e exibição de mensagem de erro em caso de falha na consulta.

        Mensagens:
            Exibe uma mensagem de erro em caso de falha na consulta.
        """
        try:

            return session.query(Contact).all()

        except IntegrityError as e:
            if session:
                session.rollback()
            print(f"Erro de integridade ao buscar dados: {e}")
            return None
        except OperationalError as e:
            if session:
                session.rollback()
            print(f"Erro operacional ao buscar dados: {e}")
            return None
        except SQLAlchemyError as e:
            if session:
                session.rollback()
            print(f"Erro SQLAlchemyao buscar dados: {e}")
            return None

    @staticmethod
    def find_contact(Contact, nome, session):
        """
        Descrição:
            A função realiza uma busca no banco de dados por um contato específico,
            com base no nome fornecido como parâmetro.

        Parâmetros:
            - Contact (Classe): A classe que representa a tabela de contatos no banco de dados.
            - parameter (str): O nome do contato que está sendo buscado.
            - session (Session): A sessão do SQLAlchemy usada para interagir com o banco de dados.

        Retorno:
            - Contact ou None: Retorna o primeiro contato encontrado que corresponda ao nome fornecido
            ou None se nenhum contato for encontrado ou se ocorrer um erro.
        """

        try:

            return session.query(Contact).filter(Contact.name == nome).first()

        except IntegrityError as e:
            if session:
                session.rollback()
            print(f"Erro de integridade ao buscar dados: {e}")
            return None
        except OperationalError as e:
            if session:
                session.rollback()
            print(f"Erro operacional ao buscar dados: {e}")
            return None
        except SQLAlchemyError as e:
            if session:
                session.rollback()
            print(f"Erro SQLAlchemyao buscar dados: {e}")
            return None

    @staticmethod
    def update_contact(contato, session):
        pass

    @staticmethod
    def delete_contact(contato, session):
        try:
            session.delete(contato)
            session.commit()
            print("@@@ Contato excluido com sucesso! @@@")
            return True
        except IntegrityError as e:
            if session:
                session.rollback()
            print(f"Erro de integridade ao excluir dados: {e}")
            return None
        except OperationalError as e:
            if session:
                session.rollback()
            print(f"Erro operacional ao excluir dados: {e}")
            return None
        except SQLAlchemyError as e:
            if session:
                session.rollback()
            print(f"Erro SQLAlchemy ao excluir dados: {e}")
            return None
