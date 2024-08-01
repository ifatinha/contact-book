"""
Módulo que representa um número de telefone.

Este módulo contém a classe Phone para mapear os dados de um telefone no banco de dados.

Classes:
    Phone: Classe para mapear os dados de um telefone no banco de dados.
"""

from dataclasses import dataclass, field
from enums.phones_types import PhonesTypes


@dataclass
class Phone:
    """
    Classe para mapear os dados de um telefone no banco de dados.

    Atributos:
        id_number (int): Identificador único do telefone no banco de dados.
        country_code (str): Código do país do telefone.
        ddd (str): Código de área do telefone (DDD).
        phone_number (str): Número do telefone.
        type_number (PhonesTypes): Tipo do telefone.
        contact (object): Contato associado ao telefone.
    """

    id_number: int = field(default=None, init=False)
    country_code: str
    ddd: str
    phone_number: str
    type_number: PhonesTypes = field(default=PhonesTypes.MOBILE)
    contact: object
