"""
Módulo que define a enumeração para os diferentes tipos de telefone.

Enumerações:
    PhoneType: Enumeração para representar os diferentes tipos de telefone.
"""

from enum import Enum


class PhonesTypes(Enum):
    """
    Enumeração para representar os diferentes tipos de telefone.

    Tipos de Telefone:
        MOBILE: Telefone celular.
        LANDLINE: Telefone fixo.
        VOIP: Telefone que utiliza a tecnologia VoIP (Voice over IP).
        FAX: Telefone utilizado para enviar e receber documentos via linha telefônica.
        SATELLITE: Telefone que se conecta diretamente aos satélites.
        EMERGENCY: Telefone de emergência utilizado em locais públicos para situações de socorro.
    """

    MOBILE = "Celular"
    LANDLINE = "Fixo"
    VOIP = "VoIP"
    FAX = "Fax"
    SATELITE = "Satélite"
    EMERGENCIA = "Emergência"
