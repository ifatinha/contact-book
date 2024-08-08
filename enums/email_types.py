"""
Módulo que define a enumeração para os diferentes tipos de emails.

Enumerações:
    EmailType: Enumeração para representar os diferentes tipos de email.
"""

from enum import Enum


class EmailTypes(Enum):
    """
    Enumeração para representar os diferentes tipos de emails.

    Tipos de Telefone:
        PERSONAL = 'Pessoal'
        WORK = 'Trabalho'
        SCHOOL = 'Escola'
        OTHER = 'Outros'
    """

    PERSONAL = "personal"
    WORK = "work"
    SCHOOL = "school"
    OTHER = "other"