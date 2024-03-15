import random
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
    change_birthday, 
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
    search_note,
    search,
)
from src.tools.helper import display_commands
from src.tools.factory import factory

sos_emojis = ["🫣", "🆘", "🚨", "❌"]

help_msg = ["🤓 How can I help you?", "🤓 Anything else?", "🤓 What else can I do for You?"]


def print_with_random_emoji(message):
    random_emoji = random.choice(sos_emojis)
    print(f"{random_emoji} {message}")


def print_with_random_help_msg():
    random_msg = random.choice(help_msg)
    print(f"{random_msg}")


def bot():
    book = factory(AddressBook, "book.bin")
    note_book = factory(NoteBook, "note-book.bin")
    print(str(book))
    print(str(note_book))
    print("😎 Welcome to the assistant bot!")

    commands = [
        "hello",
        "help",
        "add",
        "change",
        "add-email",
        "change-email",
        "phone",
        "all",
        "add-birthday",
        "show-birthday",
        "birthdays",
        "delete",
        "add-note",
        "change-note",
        "delete-note",
        "all-notes",
        "add-tag",
        "remove-tag",
        "add-address",
        "change-address",
        "search",
        "close",
        "exit",
    ]

    command_completer = WordCompleter(commands)

    while True:
        user_input = prompt("Enter a command: ", completer=command_completer)
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_to_file({"book.bin": book, "note-book.bin": note_book})
            print("😊 Good bye!")
            break
        elif command == "hello":
            print("🤓 How can I help you?")
        elif command == "help":
            display_commands()
            print_with_random_help_msg()
        elif command == "add":
            print(add_contact(args, book))
            print_with_random_help_msg()
        elif command == "change":
            print(change_contact(args, book))
            print_with_random_help_msg()
        elif command == "add-email":
            print(add_email(args, book))
            print_with_random_help_msg()
        elif command == "change-email":
            print(change_email(args, book))
            print_with_random_help_msg()
        elif command == "phone":
            print(phone(args, book))
            print_with_random_help_msg()
        elif command == "all":
            print_contacts(book)
            print_with_random_help_msg()
        elif command == "add-birthday":
            print(add_birthday(args, book))
            print_with_random_help_msg()   
        elif command == "change-birthday":
            print(change_birthday(args, book))
            print_with_random_help_msg()
        elif command == "show-birthday":
            print(show_birthday(args, book))
            print_with_random_help_msg()
        elif command == "birthdays":
            birthdays(args, book)
            print_with_random_help_msg()
        elif command == "delete":
            print(delete_contact(args, book))
            print_with_random_help_msg()
        elif command == "add-note":
            print(add_note(args, note_book))
            print_with_random_help_msg()
            print(change_note(args, note_book))
            print_with_random_help_msg()
        elif command == "delete-note":
            print(delete_note(args, note_book))
            print_with_random_help_msg()
        elif command == "all-notes":
            print(all_notes(note_book))
            print_with_random_help_msg()
        elif command == "add-tag":
            print(add_tag(args, note_book))
            print_with_random_help_msg()
        elif command == "remove-tag":
            print(remove_tag(args, note_book))
            print_with_random_help_msg()
        elif command == "add-address":
            print(add_address(args, book))
            print_with_random_help_msg()
        elif command == "change-address":
            print(change_address(args, book))
            print_with_random_help_msg()
        elif command == "search":
            print(search(args, book))
            print_with_random_help_msg()
        elif command == "search-note":
            print(search_note(args, note_book))
            print_with_random_help_msg()
        else:
            print_with_random_emoji(" Invalid command.")
