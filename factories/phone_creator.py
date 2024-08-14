"""
Este módulo fornece a classe `PhoneCreator`, que é responsável por criar objetos
de telefone com base nas entradas do usuário.

A classe `PhoneCreator` oferece métodos para:
- Exibir um menu de seleção de tipo de telefone.
- Solicitar e validar a entrada do usuário para criar um novo telefone.
- Fornecer um menu para adicionar telefones e processar a entrada até
que o usuário escolha sair.

A classe utiliza as seguintes componentes:
- `Phone`: Classe que representa um telefone e seus atributos.
- `PhonesTypes`: Enumeração que define os tipos de telefone disponíveis.

Funções principais:
- `PhoneCreator.get_phone_type()`: Exibe um menu para o usuário escolher o tipo
   de telefone e retorna o tipo selecionado.
- `PhoneCreator.get_phone()`: Solicita ao usuário os dados do telefone e
   cria uma instância de `Phone`.
- `PhoneCreator.creator_new_phone()`: Permite ao usuário adicionar novos telefones e
   continua a solicitar entradas até que o usuário opte por sair.

Exemplo de uso:
    phone = PhoneCreator.get_phone()
    print(phone)
"""

from classes.contact import Contact
from classes.phone import Phone
from classes.email import Email
from enums.phones_types import PhonesTypes


class PhoneCreator():

    """
    Classe responsável por criar instâncias de Phone com base nas entradas do usuário.
    Oferece um menu para selecionar o tipo de telefone e inserir os dados necessários
    para criar o objeto Phone.
    """

    @staticmethod
    def _prompt_type_phone():
        """
        Retorna o menu de seleção de tipo de telefone como uma string.

        Returns:
            str: O menu de seleção de tipo de telefone.
        """

        return """  # MENU ################
        [1] - Celular
        [2] - Fixo
        [3] - VoIP
        [4] - Fax
        [5] - Satélite
        [6] - Emergência
        == > """

    @staticmethod
    def _get_user_input(prompt):
        """
        Solicita uma entrada numérica do usuário com base em um prompt.

        Args:
            prompt (str): O texto a ser exibido ao usuário.

        Returns:
            int or None: O número inteiro inserido pelo usuário ou None em caso de erro.
        """

        try:
            return int(input(prompt))
        except ValueError:
            print("@@@ Entrada inválida, por favor insira um número. @@@")
            return None

    @staticmethod
    def get_phone_type():
        """
        Exibe um menu para o usuário selecionar o tipo de telefone e retorna o tipo correspondente.

        Returns:
            PhonesTypes: O tipo de telefone selecionado pelo usuário.
        """

        dict_types_phones = {
            1: PhonesTypes.MOBILE,
            2: PhonesTypes.LANDLINE,
            3: PhonesTypes.VOIP,
            4: PhonesTypes.FAX,
            5: PhonesTypes.SATELITE,
            6: PhonesTypes.EMERGENCIA,
        }

        prompt = PhoneCreator._prompt_type_phone()

        while True:

            option = PhoneCreator._get_user_input(prompt=prompt)
            if option in dict_types_phones:
                return dict_types_phones[option]
            else:
                print("@@@ Opção Inválida, tente novamente. @@@")

    @staticmethod
    def get_phone():
        """
        Solicita ao usuário os dados de um telefone (código do país, DDD, número e tipo) 
        e cria uma instância de Phone.

        Returns:
            Phone: A instância de Phone criada com os dados fornecidos pelo usuário.
        """
        country_code = input("Código do pais: ")
        ddd = input("DDD: ")
        phone_number = input("Número: ")
        type_number = PhoneCreator.get_phone_type()

        return Phone(country_code=country_code, ddd=ddd, phone_number=phone_number,
                     type_number=type_number)

    @staticmethod
    def _prompt_add_phone():
        """
        Retorna o menu de opção para adicionar um novo telefone.

        Returns:
            str: O menu para adicionar ou sair.
        """

        return """  # NOVO TELEFONE ###################
        [1] - Adicionar telefone
        [0] - Sair
        == > """

    @staticmethod
    def creator_new_phone():
        """
        Permite ao usuário adicionar novos telefones. Continua a solicitar a inserção de
        telefones até que o usuário escolha sair. Retorna uma lista com os telefones criados.

        Returns:
            list: Lista de objetos `Phone` criados pelo usuário.
        """

        phone_list = []
        prompt = PhoneCreator._prompt_add_phone()

        while True:

            option = PhoneCreator._get_user_input(prompt)

            if option == 1:
                phone = PhoneCreator.get_phone()
                phone_list.append(phone)
                print(f"Telefone: {phone} adicionado com sucesso.")
            elif option == 0:
                break
            else:
                print("@@@ Opção inválida! @@@")

        return phone_list
