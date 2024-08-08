"""
Módulo que representa um contato de agenda telefônica.

Este módulo contém a classe Contact para mapear os dados de um contato no banco de dados.

Classes:
    Contact: Classe para mapear os dados de um contato telefônico no banco de dados.
"""

from sqlalchemy import Column, Integer, String
from database.db_connection import Base


class Contact(Base):
    """
    Classe para mapear os dados de um contato no banco de dados.

    Atributos:
        contact_id (int): Identificador único do contato no banco de dados.
        contact_name (str): Nome completo do contato.
    """

    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120), nullable=False)

    def __repr__(self) -> str:
        return f"<Contact(id={self.id}, name={self.name})"
