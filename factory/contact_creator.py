from classes.contact import Contact
from classes.phone import Phone
from classes.email import Email
from enums.phones_types import PhonesTypes
from enums.email_types import EmailTypes


class ContactCreator():

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

        prompt = """################ MENU ################
        [1] - Celular
        [2] - Fixo
        [3] - VoIP
        [4] - Fax
        [5] - Satélite
        [6] - Emergência
        ==> """

        while True:
            try:
                type_phone = int(input(prompt))

                if type_phone in dict_types_phones:
                    return dict_types_phones[type_phone]
                else:
                    print("@@@ Opção Inválida, tente novamente. @@@")
            except ValueError:
                print("@@@ Entrada inválida, por favor insira um número. @@@")

    @staticmethod
    def get_phone():
        country_code = input("Código do pais: ")
        ddd = input("DDD: ")
        phone_number = input("Número: ")
        phone_type = ContactCreator.get_phone_type()

        return Phone(country_code=country_code, ddd=ddd, phone_number=phone_number,  type_number=phone_type)

    # @staticmethod
    # def get_email():
    #     pass

    # @staticmethod
    # def get_instance_contact():
    #     print("################# NOVO CONTATO #################")

    #     nome = input("Nome: ")
