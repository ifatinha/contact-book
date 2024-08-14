from classes.contact import Contact
from classes.phone import Phone
from classes.email import Email
from enums.phones_types import PhonesTypes


class PhoneCreator():

    @staticmethod
    def _generate_prompt():
        return """################ MENU ################
        [1] - Celular
        [2] - Fixo
        [3] - VoIP
        [4] - Fax
        [5] - Satélite
        [6] - Emergência
        ==> """

    @staticmethod
    def _get_user_input(prompt):
        try:
            return int(input(prompt))
        except ValueError:
            print("@@@ Entrada inválida, por favor insira um número. @@@")
            return None

    @staticmethod
    def get_phone_type():
        dict_types_phones = {
            1: PhonesTypes.MOBILE,
            2: PhonesTypes.LANDLINE,
            3: PhonesTypes.VOIP,
            4: PhonesTypes.FAX,
            5: PhonesTypes.SATELITE,
            6: PhonesTypes.EMERGENCIA,
        }

        prompt = PhoneCreator._generate_prompt()

        while True:

            option = PhoneCreator._get_user_input(prompt=prompt)
            if option in dict_types_phones:
                return dict_types_phones[option]
            else:
                print("@@@ Opção Inválida, tente novamente. @@@")

    @staticmethod
    def get_phone():
        country_code = input("Código do pais: ")
        ddd = input("DDD: ")
        phone_number = input("Número: ")
        type_number = PhoneCreator.get_phone_type()

        return Phone(country_code=country_code, ddd=ddd, phone_number=phone_number,
                     type_number=type_number)

    @staticmethod
    def new_phone_prompt():
        return """################### NOVO TELEFONE ###################
        [1] - Novo telefone
        [2] - Sair
        ==> """

    @staticmethod
    def creator_new_phone():

        while True:

            prompt = PhoneCreator.new_phone_prompt()

            try:
                option = PhoneCreator._get_user_input(prompt)
            except ValueError:
                print("@@@ Entrada inválida, por favor insira um número. @@@")
                continue

            if option == 1:
                phone = PhoneCreator.get_phone()
                return phone
            elif option == 0:
                break
            else:
                print("@@@ Opção inválida! @@@")
