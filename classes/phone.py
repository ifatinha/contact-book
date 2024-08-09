"""
Módulo que representa um número de telefone.

Este módulo contém a classe Phone para mapear os dados de um telefone no banco de dados.

Classes:
    Phone: Classe para mapear os dados de um telefone no banco de dados.
"""

from sqlalchemy import Column, Integer, String, ForeignKey, Enum as SQLAEnum
from database.db_connection import Base
from enums.phones_types import PhonesTypes


class Phone(Base):
    """
    Classe para mapear os dados de um telefone no banco de dados.

    Atributos:
        id_number (int): Identificador único do telefone no banco de dados.
        country_code (str): Código do país do telefone.
        ddd (str): Código de área do telefone (DDD).
        phone_number (str): Número do telefone.
        type_number (PhonesTypes): Tipo do telefone (Móvel, Residencial, Comercial, etc.).
        contact_id (int): Chave estrangeira associada ao contato.
    """

    __tablename__ = "phones"

    id_number = Column(Integer, primary_key=True, autoincrement=True)
    country_code = Column(String(8), nullable=False)
    ddd = Column(String(8), nullable=False)
    phone_number = Column(String(16), nullable=False)
    type_number = Column(SQLAEnum(PhonesTypes), default=PhonesTypes.MOBILE, nullable=False)
    contact_id = Column(Integer, ForeignKey("contacts.id"), nullable=False)

    def __repr__(self) -> str:
        return (
            f"<Phone(id_number={self.id_number}, country_code={self.country_code}, "
            f"ddd={self.ddd}, phone_number={self.phone_number}, "
            f"type_number={self.type_number.name}, contact_id={self.contact_id})>"
        )

    def __str__(self) -> str:
        """
        Retorna uma string legível representando o telefone no formato:
        +<country_code> (<ddd>) <phone_number> - <type_number>

        Exemplo: +1 (212) 555-1234 - MOBILE
        """
        return f"+{self.country_code} ({self.ddd}) {self.phone_number} - {self.type_number}"
