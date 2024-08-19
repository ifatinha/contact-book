"""
Módulo que representa um número de telefone.

Este módulo contém a classe Phone para mapear os dados de um telefone no banco de dados.

Classes:
    Phone: Classe para mapear os dados de um telefone no banco de dados.
"""

from sqlalchemy import Column, Integer, String, ForeignKey, Enum as SQLAEnum, DateTime
from database.db_connection import Base
from enums.phones_types import PhonesTypes
from sqlalchemy.orm import relationship
from datetime import datetime


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
        created_at (Date): Data que o Objeto foi criado.
        update_at (Date): Data da ultima atualização no banco de dados.
    """

    __tablename__ = 'phones'
    id_phone = Column(Integer, primary_key=True, autoincrement=True)
    country_code = Column(String(8), nullable=False)
    ddd = Column(String(8), nullable=False)
    phone_number = Column(String(16), nullable=False)
    type_number = Column(SQLAEnum(PhonesTypes), default=PhonesTypes.MOBILE, nullable=False)
    contact_id = Column(Integer, ForeignKey('contacts.id'))
    contact = relationship("Contact", back_populates="phones")
    created_at = Column(DateTime, default=datetime.now())
    update_at = Column(DateTime, default=datetime.now())

    def __repr__(self) -> str:
        return (
            f"<Phone(id_number={self.id_phone}, country_code={self.country_code}, "
            f"ddd={self.ddd}, phone_number={self.phone_number}, "
            f"type_number={self.type_number.name}, contact_id={self.contact_id})>"
        )

    def __str__(self) -> str:
        """
        Retorna uma string legível representando o telefone no formato:
        +<country_code> (<ddd>) <phone_number> - <type_number>

        Exemplo: +1 (212) 555-1234 - MOBILE
        """
        return f"{self.id_phone}. (+{self.country_code} ({self.ddd}) {self.phone_number} - {self.type_number.value})"
