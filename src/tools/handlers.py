import pickle
from src.tools.input_error import input_error, input_error_days
from src.tools.note_input_error import note_input_error
from src.tools.input_error_address import input_error_address
from src.classes.addressBook import AddressBook
from src.classes.noteBook import NoteBook
from src.classes.record import Record
from src.classes.note import Note
from src.classes.book import Book


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
def delete_contact(args, book:AddressBook):
    if len(args) == 0:
        return "Give me user name please."
    name, = args
    book.delete(name)
    return f"Contact {name} is deleted."

@input_error
def change_contact(args, book: AddressBook):
    name, phone, new_phone = args
    record = book.find(name)
    if not record:
        raise ValueError(f"Contact {name} doesn't exist. Please add contact first")
    record.edit_phone(phone, new_phone)
    return "Contact is changed."


@input_error
def add_email(args, book: AddressBook):
    if len(args) != 2:
        return "Give me name and email address please."
    name, email = args
    record = book.find(name)
    if not record:
        raise ValueError(f"Contact {name} doesn't exist. Please add contact first")
    record.add_email(email)
    return "Email is added"

@input_error
def change_email(args, book: AddressBook):
    if len(args) != 3:
        return "Give me name old email and new email address please."
    name, email, new_email = args
    record = book.find(name)
    if not record:
        raise ValueError(f"Contact {name} doesn't exist. Please add contact first")
    record.change_email(email, new_email)
    return "Email is changed."

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

@input_error_days
def birthdays(args, book: AddressBook):
    days, = args
    if len(book) > 0:
        book.get_birthdays_per_days(days)
    else: 
        print("No added contacts yet")

@note_input_error
def add_note(args, note_book: NoteBook):
    name = " ".join(args).strip()
    description = input("Enter a description: ")
    note = note_book.find(name)
    if not note:
        note = Note(name, description)
    note_book.add_record(note)
    return "Note is added."


@note_input_error
def add_tag(args, note_book: NoteBook):
    note, tag = args
    record = note_book.find(note)
    if not record:
        raise ValueError(f"Note for {note} doesn't exist. Please add note first")
    note.add_tag(tag)


@note_input_error
def remove_tag(args, note_book: NoteBook):
    note, tag_to_remove = args
    record = note_book.find(note)
    if not record:
        raise ValueError(f"Note for {note} doesn't exist. Please add note first")
    note.remove_tag(tag_to_remove)
    return f"Tag {tag_to_remove} removed."


def all_notes(note_book: NoteBook):
    if len(note_book) > 0:
        print(str(note_book))
    else:
        print("No added notes yet")

@note_input_error
def change_note(args, note_book: NoteBook):
    name = " ".join(args).strip()
    new_description = input("Enter a description: ")
    note = note_book.find(name)
    if not note:
        raise ValueError(f"Note {name} is not added yet. Please add note first")
    note.change_description(new_description)
    return "Note is changed."

@note_input_error
def delete_note(args, note_book: NoteBook):
    name = " ".join(args).strip()
    note = note_book.find(name)
    if not note:
        raise ValueError(f"Note {name} is not added yet. Please add note first")
    note_book.delete(name)
    return f"Note {note} is deleted."


@input_error_address
def add_address(args, book: AddressBook):
    """adds address to contact"""
    name, address = args
    record = book.find(name)
    if not record:
        raise ValueError(f"Contact {name} doesn't exist. Please add contact first")
    record.add_postal_address(address)
    return f"{name}`s address is added"


@input_error_address
def change_address(args, book: AddressBook):
    """changes existing address of contact"""
    name, new_address = args
    record = book.find(name)
    if not record:
        raise ValueError(f"Contact {name} doesn't exist. Please add contact first")
    record.edit_postal_address(new_address)
    return f"{name}`s address is changed."

def search(args, book: AddressBook):
    search_string, = args
    book.search_contact(search_string)
    
def search_note(args, note_book: NoteBook):
    search_string, = args
    note_book.search_note(search_string)

def save_to_file(files):
    for f, book in files.items():
        with open(f, 'wb') as file:
            pickle.dump(book, file)
