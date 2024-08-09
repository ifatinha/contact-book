"""
    Classe de teste
"""

# from database.db_create import DBCreate
# DBCreate.check_and_create_database("contact-book")

# from database.db_connection import engine, Base, get_session
from classes.contact import Contact
# from classes.email import Email
# from classes.phone import Phone
# from enums.phones_types import PhonesTypes
# from enums.email_types import EmailTypes
from database.db_operations import DBOperation

# Criando todas as tabelas do banco de dados (se elas ainda nao existirem)
# Base.metadata.create_all(engine)

# new_contact = Contact(name="Marcus Monteiro")

# phone1 = Phone(country_code="+55", ddd="69", phone_number="98051-0109",
#                type_number=PhonesTypes.MOBILE)
# phone2 = Phone(country_code="+55", ddd="69", phone_number="2885-4727",
#                type_number=PhonesTypes.LANDLINE)

# email1 = Email(email="joao.silva@example.com", type_email=EmailTypes.PERSONAL)
# email2 = Email(email="jsilva@empresa.com", type_email=EmailTypes.WORK)

# new_contact.phones = [phone1, phone2]
# new_contact.emails = [email1, email2]

# DBOperation.save_obj_db(new_contact)

print(DBOperation.find_objs_db(Contact))