"""
Módulo que representa um e-mail.

Este módulo contém a classe Email para mapear os dados de um e-mail no banco de dados.

Classes:
    Email: Classe para mapear os dados de um e-mail no banco de dados.
"""

from sqlalchemy import Column, Integer, String, ForeignKey, Enum as SQLAEnum, DateTime
from database.db_connection import Base
from enums.email_types import EmailTypes
from sqlalchemy.orm import relationship
from datetime import datetime


class Email(Base):
    """
    Classe para mapear os dados de um e-mail no banco de dados.

    Atributos:
        id_number (int): Identificador único do e-mail no banco de dados.
        email (str): Endereço de e-mail.
        type_email (EmailTypes): Tipo do e-mail (Pessoal, Comercial, etc.).
        contact_id (int): Chave estrangeira associada ao contato.
        created_at (Date): Data que o Objeto foi criado.
        update_at (Date): Data da ultima atualização no banco de dados.
    """

    __tablename__ = 'emails'

    id_email = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(120), nullable=False)
    type_email = Column(SQLAEnum(EmailTypes), default=EmailTypes.PERSONAL, nullable=False)
    contact_id = Column(Integer, ForeignKey('contacts.id'))
    contact = relationship("Contact", back_populates="emails")
    created_at = Column(DateTime, default=datetime.now())
    update_at = Column(DateTime, default=datetime.now())

    def __repr__(self) -> str:
        return (
            f"<Email(id_email={self.id_email}, email={self.email}, "
            f"type_email={self.type_email.name}, contact_id={self.contact_id})>"
        )

    def __str__(self) -> str:
        """
        Retorna uma string legível representando o e-mail no formato:
        <email> - <type_email>

        Exemplo: joao.silva@example.com - PESOAL
        """
        return f"{self.id_email}. ({self.email} - {self.type_email.value})"
