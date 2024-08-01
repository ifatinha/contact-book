"""
Módulo que representa um e-mail.

Este módulo contém a classe Email para mapear os dados de um e-mail no banco de dados.

Classes:
    Email: Classe para mapear os dados de um e-mail no banco de dados.
"""

from dataclasses import dataclass, field
from enums.email_types import EmailTypes


@dataclass
class Email:
    """
    Classe para mapear os dados de um e-mail no banco de dados.

    Atributos:
        id_number (int): Identificador único do e-mail no banco de dados.
        email (str): Endereço de e-mail.
        type_email (EmailTypes): Tipo do e-mail.
        contact (object): Contato associado ao e-mail.
    """

    id_number: int = field(default=None, init=False)
    email: str
    type_email: EmailTypes = field(default=EmailTypes.PERSONAL)
    contact: object
