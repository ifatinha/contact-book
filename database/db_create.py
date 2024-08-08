import mysql.connector
import mysql.connector.errorcode
import logging
from mysql.connector import Error
from pathlib import Path
from database.config import DATABASE_CONFIG

# Configuração básica do logging para registrar em um arquivo
file_path = Path(__file__).resolve().parents[1] / "logs" / "mysql_logs.log"

logging.basicConfig(
    filename=file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class DBCreate():

    @staticmethod
    def get_connect():
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
        """Fecha a conexão com o servidor MySQL."""
        if conn is not None and conn.is_connected():
            conn.close()
            logging.info("Conexão fechada.")
        else:
            logging.info("A conexão já estava fechada ou não foi estabelecida.")

    @staticmethod
    def check_and_create_database(db_name):
        """Verifica se um banco de dados existe e, se não, cria-o."""

        conn = DBCreate.get_connect()
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
                DBCreate.get_close(conn)
                logging.info("Cursor fechado.")
