"""
Módulo que representa um contato de agenda telefônica.

Este módulo contém a classe Contact para mapear os dados de um contato no banco de dados.

Classes:
    Contact: Classe para mapear os dados de um contato telefônico no banco de dados.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.db_connection import Base


class Contact(Base):
    """
    Classe para mapear os dados de um contato no banco de dados.

    Atributos:
        id (int): Identificador único do contato no banco de dados.
        name (str): Nome completo do contato.
        phones (list[Phone]): Lista de números de telefone associados ao contato.
        emails (list[Email]): Lista de e-mails associados ao contato.
    """

    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120), nullable=False)
    phones = relationship("Phone", back_populates="contact", cascade="all, delete-orphan")
    emails = relationship("Email", back_populates="contact", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"Contact(id={self.id}, name={self.name})"

    def __str__(self) -> str:
        """
        Retorna uma string legível representando o contato no formato:
        Nome: <name>, Telefones: [<phone1>, <phone2>, ...], E-mails: [<email1>, <email2>, ...]

        Exemplo: Nome: João Silva,
                 Telefones: [+1 (212) 555-1234 - MOBILE, +1 (213) 555-5678 - HOME],
                 E-mails: [joao.silva@example.com, jsilva@work.com]
        """
        phones_str = ", ".join(str(phone) for phone in self.phones) if self.phones else "Nenhum telefone"
        emails_str = ", ".join(str(email) for email in self.emails) if self.emails else "Nenhum e-mail"
        return f"Nome: {self.name}, Telefones: [{phones_str}], E-mails: [{emails_str}]"
