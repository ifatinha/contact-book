"""
    Classe para gerenciar a criação e conexão com um banco de dados MySQL.

    Esta classe fornece métodos estáticos para:
    - Estabelecer uma conexão com o servidor MySQL.
    - Fechar uma conexão com o servidor MySQL.
    - Verificar a existência de um banco de dados específico e, se não existir, criá-lo.

    A configuração da conexão é obtida a partir do módulo `database.config`,
    onde as credenciais e informações do banco de dados são armazenadas.

    Métodos:
        - get_connect: Estabelece uma conexão com o MySQL usando as configurações fornecidas.
        - get_close: Fecha a conexão com o servidor MySQL.
        - check_and_create_database: Verifica se um banco de dados com o nome especificado existe e,
        se não, cria-o.
    """

from mysql.connector import Error
import mysql.connector
import mysql.connector.errorcode
from database.config import DATABASE_CONFIG
from util.logging_config import setup_logging
import logging

# Configuração do loggin
setup_logging()
mysql_logger = logging.getLogger('mysql')


class DBCreated():

    """
    Classe para gerenciamento da criação e conexão com um banco de dados MySQL.
    """

    @staticmethod
    def get_connect():
        """
        Estabelece uma conexão com o servidor MySQL.

        Retorna:
            mysql.connector.connection_cext.CMySQLConnection: Objeto de conexão com o MySQL
            se a conexão for bem-sucedida, None caso contrário.
        """

        connection = None

        try:
            connection = mysql.connector.connect(
                user=DATABASE_CONFIG["user"],
                password=DATABASE_CONFIG["password"],
                host=DATABASE_CONFIG["host"]
                # dabatase=DATABASE_CONFIG["database"]
            )

            if connection.is_connected():
                logging.info("Conexão bem-sucedida!")
                return connection

        except mysql.connector.Error as error:
            logging.error("Erro ao conectar o banco de dados %s", error)

        return None

    @staticmethod
    def get_close(conn):
        """
        Fecha a conexão com o servidor MySQL.

        Args:
            conn (mysql.connector.connection_cext.CMySQLConnection):
                Objeto de conexão com o MySQL a ser fechado.
        """

        if conn is not None and conn.is_connected():
            conn.close()
            logging.info("Conexão fechada.")
        else:
            logging.info("A conexão já estava fechada ou não foi estabelecida.")

    @staticmethod
    def check_and_create_database(db_name):
        """
        Verifica se um banco de dados existe e, se não, cria-o.

        Args:
            db_name (str): Nome do banco de dados a ser verificado e possivelmente criado.
        """

        conn = DBCreated.get_connect()

        if conn is None:
            logging.error("Não foi possível estabelecer uma conexão com o MySQL.")
            return

        cursor = conn.cursor()

        try:
            cursor.execute(f"SHOW DATABASES LIKE '{db_name}';")
            result = cursor.fetchone()

            if result:
                logging.info("O bando de dados '%s' já existe.", db_name)
                logging.info("Estabelecendo conexão.")
            else:
                logging.info("O banco de dados '%s' não existe.", db_name)
                logging.info("Criando banco de dados.")
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}`;")
                logging.info("Banco de dados '%s' criado com sucesso!", db_name)
        except Error as err:
            if err.errno == mysql.connector.errorcode.ER_DB_CREATE_EXISTS:
                logging.error("Erro ao verificar/criar banco de dados: %s.", err)
            else:
                logging.error("Erro ao criar o banco de dados: %s.", err)
        finally:
            if cursor is not None:
                cursor.close()
                DBCreated.get_close(conn)
                logging.info("Cursor fechado.")
