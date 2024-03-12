from src.tools.input_error import input_error
from src.classes.addressBook import AddressBook
from src.classes.record import Record


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, book: AddressBook):
    name, phone = args
    record = book.find(name)
    if not record:
        record = Record(name)
    record.add_phone(phone)
    book.add_record(record)
    return "Contact added."


@input_error
def change_contact(args, book: AddressBook):
    name, phone, new_phone = args
    record = book.find(name)
    if not record:
        raise ValueError(f"Contact {name} doesn't exist. Please add contact first")
    record.edit_phone(phone, new_phone)
    return "Contact is changed."


@input_error
def phone(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if not record:
        raise ValueError(f"Contact {name} doesn't exist. Please add contact first")
    return str(record)


def print_contacts(book: AddressBook):
    if len(book) > 0:
        print(str(book))
    else:
        print("No added contacts yet")


@input_error
def add_birthday(args, book: AddressBook):
    name, birthday = args
    record = book.find(name)
    if not record:
        raise ValueError(f"Contact {name} doesn't exist. Please add contact first")
    record.add_birthday(birthday)
    return "Birthday is added"


@input_error
def show_birthday(args, book: AddressBook):
    (name,) = args
    record = book.find(name)
    if not record:
        raise ValueError(f"Contact {name} doesn't exist. Please add contact first")
    if not record.birthday:
        raise ValueError(
            f"Birthday for contact {name} is not added yet. Please add birthday first"
        )
    return f"Contact {name} birthday is: {str(record.birthday)}"


def birthdays(book: AddressBook):
    if len(book) > 0:
        book.get_birthdays_per_week()
    else:
        print("No added contacts yet")

# add handler for add-address, change-address

def add_address(args, book: AddressBook):
    """adds address to contact"""
    name, address = args
    record = book.find(name)
    if not record:
        raise ValueError(f"Contact {name} doesn't exist. Please add contact first")
    record.add_postal_address(address)
    return f"{name}`s address is added"

def change_address(args, book: AddressBook):
    """changes existing address of contact"""
    name, new_address = args
    record = book.find(name)
    if not record:
        raise ValueError(f"Contact {name} doesn't exist. Please add contact first")
    record.edit_postal_address(new_address)
    return f"{name}`s address is changed."
