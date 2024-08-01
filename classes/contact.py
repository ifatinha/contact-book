"""
Módulo que representa um contato de agenda telefônica.

Este módulo contém a classe Contact para mapear os dados de um contato no banco de dados.

Classes:
    Contact: Classe para mapear os dados de um contato telefônico no banco de dados.
"""

from dataclasses import dataclass, field


@dataclass
class Contact:
    """
    Classe para mapear os dados de um contato no banco de dados.

    Atributos:
        contact_id (int): Identificador único do contato no banco de dados.
        contact_name (str): Nome completo do contato.
    """

    contact_id: int = field(default=None, init=False)
    contact_name: str
