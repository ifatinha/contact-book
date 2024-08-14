"""
Este módulo fornece a classe `EmailCreator`, que é responsável por criar objetos
de email com base nas entradas do usuário.

A classe `EmailCreator` oferece métodos para:
- Exibir um menu de seleção de tipo de email.
- Solicitar e validar a entrada do usuário para criar um novo email.
- Fornecer um menu para adicionar emails e processar a entrada até
que o usuário escolha sair.

A classe utiliza os seguintes componentes:
- `Email`: Classe que representa um email e seus atributos.
- `EmailTypes`: Enumeração que define os tipos de emails disponíveis.

Funções principais:
- `EmailCreator.get_email_type()`: Exibe um menu para o usuário escolher o tipo
   de email e retorna o tipo selecionado.
- `EmailCreator.get_email()`: Solicita ao usuário os dados do email e
   cria uma instância de `Email`.
- `EmailCreator.created_emails()`: Permite ao usuário adicionar novos emails e
   continua a solicitar entradas até que o usuário opte por sair.

Exemplo de uso:
    email = EmailCreator.get_email()
    print(phone)
    emails = EmailCreator.created_emails()
    print(emails)
"""

# flake8: noqa: F401
from classes.contact import Contact
from classes.phone import Phone
from classes.email import Email
from enums.email_types import EmailTypes
from util.prompts import get_user_input


class EmailCreator():

    """
    Classe responsável pela criação e gestão de emails. 

    Oferece métodos estáticos para solicitar informações ao usuário e criar instâncias da classe `Email`. 
    Inclui funcionalidades para definir o tipo de email e gerenciar a entrada de múltiplos emails.
    """

    @staticmethod
    def _prompt_type_email():
        """
        Retorna o prompt para seleção do tipo de email.

        :return: String com o prompt de seleção de tipo de email.
        """

        return """  # TIPO DE EMAIL ################
        [1] - Pessoal
        [2] - Trabalho
        [3] - Outros
        ==> """

    @staticmethod
    def _get_email_type():
        """
        Obtém o tipo de email do usuário e retorna o correspondente.

        :return: EmailTypes correspondente à opção escolhida pelo usuário.
        """
        dict_types_emails = {
            1: EmailTypes.PERSONAL,
            2: EmailTypes.WORK,
            3: EmailTypes.OTHER
        }

        prompt = EmailCreator._prompt_type_email()

        while True:
            option = get_user_input(prompt=prompt)
            if option in dict_types_emails:
                return dict_types_emails[option]
            else:
                print("@@@ Opção Inválida, tente novamente. @@@")

    @staticmethod
    def get_email():
        """
        Solicita ao usuário os dados do email e retorna um objeto Email.

        :return: Instância da classe Email com os dados fornecidos pelo usuário.
        """
        email = input("Email: ")
        type_email = EmailCreator._get_email_type()

        return Email(email=email, type_email=type_email)

    @staticmethod
    def _prompt_add_email():
        """
        Retorna o prompt para adicionar um novo email ou sair.

        :return: String com o prompt para adicionar email ou sair.
        """

        return """  # NOVO EMAIL ###################
        [1] - Add email
        [0] - Sair
        == > """

    @staticmethod
    def created_emails() -> list[Email]:
        """
        Cria e retorna uma lista de emails conforme a entrada do usuário.

        :return: Lista de instâncias da classe Email.
        """

        emails = []
        prompt = EmailCreator._prompt_add_email()

        while True:

            option = get_user_input(prompt=prompt)

            if option == 1:
                email = EmailCreator.get_email()
                emails.append(email)
                print(f"Email ({email}) cadastrado com sucesso!")
            elif option == 0:
                break
            else:
                print("@@@ Opção inválida! @@@")

        return emails
