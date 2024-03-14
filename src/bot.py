from re import search
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

from src.classes.addressBook import AddressBook
from src.classes.noteBook import NoteBook

from src.tools.handlers import (
    add_address, 
    add_birthday, 
    add_contact,
    add_email, 
    add_note,
    all_notes, 
    birthdays, 
    change_contact,
    change_email,
    change_note,
    delete_note, 
    parse_input, 
    phone, 
    print_contacts,
    save_to_file, 
    show_birthday, 
    change_address,
    delete_contact,
    add_tag,
    remove_tag,
    )
from src.tools.factory import factory



def bot():
    book = factory(AddressBook, 'book.bin')
    note_book = factory(NoteBook, 'note-book.bin')
    print(str(book))
    print(str(note_book))
    print("Welcome to the assistant bot!")

    commands = [
    "hello", "help","add", "change", "add-email", "change-email", "phone",
    "all", "add-birthday", "show-birthday", "birthdays", "delete",
    "add-note", "change-note", "delete-note", "all-notes", "add-tag",
    "remove_tag", "add-address", "change-address", "search", "close",
    "exit"
]

    command_completer = WordCompleter(commands)

    while True:
        user_input = prompt("Enter a command: ", completer=command_completer)
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_to_file({"book.bin": book, "note-book.bin": note_book})
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
            print("How can I help you?")
        elif command == "change":
            print(change_contact(args, book))
            print("How can I help you?")
        elif command == "add-email":
            print(add_email(args, book))
            print("How can I help you?")
        elif command == "change-email":
            print(change_email(args, book))
            print("How can I help you?")
        elif command == "phone":
            print(phone(args, book))
            print("How can I help you?")
        elif command == "all":
            print_contacts(book)
            print("How can I help you?")
        elif command == "add-birthday":
            print(add_birthday(args, book))
            print("How can I help you?")
        elif command == "show-birthday":
            print(show_birthday(args, book))
            print("How can I help you?")
        elif command == "birthdays":
            birthdays(args, book)
            print("How can I help you?")
        elif command == "delete":
            print(delete_contact(args, book))
            print("How can I help you?")
        elif command == "add-note":
            print(add_note(args, note_book))
            print("How can I help you?")
        elif command == "change-note":
            print(change_note(args, note_book))
            print("How can I help you?")
        elif command == "delete-note":
            print(delete_note(args, note_book))
            print("How can I help you?")
        elif command == "all-notes":
            print(all_notes(note_book))
        elif command == "add-tag":
            print(add_tag(args, note_book))
            print("How can I help you?")
        elif command == "remove_tag":
            print(remove_tag(args, note_book))
            print("How can I help you?")
        elif command == "add-address":
            print(add_address(args, book))
            print("How can I help you?")
        elif command == "change-address":
            print(change_address(args, book))
            print("How can I help you?")
        elif command == "search":
            print(search(args, book))
            print("How can I help you?")
        else:
            print("Invalid command.")
