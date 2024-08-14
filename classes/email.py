"""
Módulo que representa um e-mail.

Este módulo contém a classe Email para mapear os dados de um e-mail no banco de dados.

Classes:
    Email: Classe para mapear os dados de um e-mail no banco de dados.
"""

from sqlalchemy import Column, Integer, String, ForeignKey, Enum as SQLAEnum
from database.db_connection import Base
from enums.email_types import EmailTypes
from sqlalchemy.orm import relationship


class Email(Base):
    """
    Classe para mapear os dados de um e-mail no banco de dados.

    Atributos:
        id_number (int): Identificador único do e-mail no banco de dados.
        email (str): Endereço de e-mail.
        type_email (EmailTypes): Tipo do e-mail (Pessoal, Comercial, etc.).
        contact_id (int): Chave estrangeira associada ao contato.
    """

    __tablename__ = 'emails'

    id_number = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(120), nullable=False)
    type_email = Column(SQLAEnum(EmailTypes), default=EmailTypes.PERSONAL, nullable=False)
    contact_id = Column(Integer, ForeignKey('contacts.id'))
    contact = relationship("Contact", back_populates="emails")

    def __repr__(self) -> str:
        return (
            f"<Email(id_number={self.id_number}, email={self.email}, "
            f"type_email={self.type_email.name}, contact_id={self.contact_id})>"
        )

    def __str__(self) -> str:
        """
        Retorna uma string legível representando o e-mail no formato:
        <email> - <type_email>

        Exemplo: joao.silva@example.com - PERSONAL
        """
        return f"{self.email} - {self.type_email.name}"
