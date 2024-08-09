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
    - `DBOperation.object_save_db(obj)`: Adiciona o objeto especificado ao banco de dados e faz commit,
       tratando exceções em caso de erro.

Exemplo:
    # Criar o esquema
    DBOperation.create_schema()

    # Adicionar um novo contato
    novo_contato = Contact(name="João Silva")
    DBOperation.object_save_db(novo_contato)
"""

from sqlalchemy.exc import SQLAlchemyError, IntegrityError, OperationalError
from database.db_connection import get_session


class DBOperation():

    """
    Classe para operações básicas de banco de dados usando SQLAlchemy.

    Métodos Estáticos:
        session: Cria e retorna uma nova sessão do banco de dados.
        object_save_db: Adiciona um objeto à base de dados e faz commit.
    """

    @staticmethod
    def session():
        """
        Cria e retorna uma nova sessão do banco de dados.

        Retorna:
            session (Session): Instância da sessão SQLAlchemy.
        """
        return get_session()

    @staticmethod
    def save_obj_db(obj):
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
            session = DBOperation.session()
            session.add(obj)
            session.commit()
            print(f"{obj.__class__.__name__} Cadastrado com sucesso!")
        except IntegrityError as e:
            session.rollback()
            print(f"Erro de integridade ao adicionar contato: {e}")
        except OperationalError as e:
            session.rollback()
            print(f"Erro operacional ao adicionar contato: {e}")
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Erro SQLAlchemy ao adicionar contato: {e}")
        finally:
            session.close()

    @staticmethod
    def find_objs_db(model):
        """
        Busca todos os objetos de uma tabela do banco de dados.

        Parâmetros:
            model (Base): Classe do modelo a ser consultado,
            que deve ser uma subclasse de `Base` do SQLAlchemy.

        Retorna:
            list: Lista de instâncias do modelo consultado.

        Exceções:
            Rollback e exibição de mensagem de erro em caso de falha na consulta.

        Mensagens:
            Exibe uma mensagem de erro em caso de falha na consulta.
        """
        try:
            session = DBOperation.session()
            return session.query(model).all()

        except IntegrityError as e:
            if session:
                session.rollback()
            print(f"Erro de integridade ao adicionar contato: {e}")
            return None
        except OperationalError as e:
            if session:
                session.rollback()
            print(f"Erro operacional ao adicionar contato: {e}")
            return None
        except SQLAlchemyError as e:
            if session:
                session.rollback()
            print(f"Erro SQLAlchemy ao adicionar contato: {e}")
            return None
        finally:
            if session:
                # session.close()
                pass
