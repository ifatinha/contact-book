# logging_config.py
import logging
from pathlib import Path


def setup_logging():
    """
    Configura o logging para o projeto.
    """
    # Caminho para a raiz do projeto e configuração do diretório de logs
    project_root = Path(__file__).resolve().parents[1]
    log_dir = project_root / "logs"
    sqlalchemy_log_file = log_dir / "sqlalchemy.log"
    mysql_log_file = log_dir / "mysql.log"

    # Criar o diretório de logs se não existir
    log_dir.mkdir(parents=True, exist_ok=True)

    # Remover todos os manipuladores do logger root para evitar duplicação
    for handler in logging.getLogger().handlers[:]:
        logging.getLogger().removeHandler(handler)

    # Configurar o logger para o SQLAlchemy
    sqlalchemy_logger = logging.getLogger('sqlalchemy')
    sqlalchemy_logger.setLevel(logging.DEBUG)  # Captura todos os logs de DEBUG para o SQLAlchemy
    sqlalchemy_file_handler = logging.FileHandler(sqlalchemy_log_file)
    sqlalchemy_file_handler.setLevel(logging.DEBUG)
    sqlalchemy_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    sqlalchemy_file_handler.setFormatter(sqlalchemy_formatter)
    sqlalchemy_logger.addHandler(sqlalchemy_file_handler)
    sqlalchemy_logger.propagate = False

    # Configurar o logger para o MySQL
    mysql_logger = logging.getLogger('mysql')
    mysql_logger.setLevel(logging.DEBUG)
    mysql_file_handler = logging.FileHandler(mysql_log_file)
    mysql_file_handler.setLevel(logging.DEBUG)
    mysql_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    mysql_file_handler.setFormatter(mysql_formatter)
    mysql_logger.addHandler(mysql_file_handler)
    mysql_logger.propagate = False

    # Configurar o nível do logger root para evitar logs no terminal
    logging.basicConfig(level=logging.CRITICAL)  # Define o nível do logger root para CRITICAL
