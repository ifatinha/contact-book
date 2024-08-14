
# flake8: noqa: F401
from classes.contact import Contact
from classes.phone import Phone
from classes.email import Email
from factory.email_creator import EmailCreator
from factory.phone_creator import PhoneCreator


class ContactCreator():

    @staticmethod
    def get_instance_contact():
        print("################# NOVO CONTATO #################")

        name = input("Nome: ")
        phones = PhoneCreator.created_phones()
        emails = EmailCreator.created_emails()

        return Contact(name=name, phones=phones, emails=emails)
