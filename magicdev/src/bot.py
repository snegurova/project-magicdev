from pathlib import Path
from random import choice
from re import search
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style
from ascii_magic import AsciiArt

from .classes.addressBook import AddressBook
from .classes.noteBook import NoteBook

from .tools.colors import green, red
from .tools.handlers import (
    add_address,
    add_birthday,
    add_contact,
    add_email,
    add_note,
    all_notes,
    birthdays,
    change_contact,
    change_birthday,
    change_email,
    delete_email,
    change_note,
    delete_note,
    find_note,
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
from .tools.helper import display_commands
from .tools.factory import factory

sos_emojis = ["🫣", "🆘", "🚨", "❌"]

help_msg = ["🤓 How can I help you?", "🤓 Anything else?", "🤓 What else can I do for You?"]

dev_image_path = Path(__file__).parent / "tools/dev.jpg"
dev_image = AsciiArt.from_image(dev_image_path)

def print_with_random_emoji(message):
    random_emoji = choice(sos_emojis)
    print(f"{random_emoji} {message}")


def print_with_random_help_msg():
    random_msg = choice(help_msg)
    print(f"\n{random_msg}")

def bot(book_file, note_book_file):
    book = factory(AddressBook, book_file)
    note_book = factory(NoteBook, note_book_file)
    dev_image.to_terminal()
    print(green("😎 Welcome to the assistant bot!"))

    commands = [
        "hello",
        "help",
        "add",
        "change",
        "add-email",
        "change-email",
        "delete-email",
        "phone",
        "all",
        "add-birthday",
        "show-birthday",
        "change-birthday",
        "birthdays",
        "delete",
        "add-note",
        "change-note",
        "delete-note",
        "find-note",
        "all-notes",
        "add-tag",
        "remove-tag",
        "add-address",
        "change-address",
        "search",
        "search-note",
        "close",
        "exit",
    ]

    command_completer = WordCompleter(commands, sentence = True)

    while True:
        style = Style.from_dict({"text": "ansicyan"})
        text = [("class:text", "Enter a command: ")]
        user_input = prompt(text, completer=command_completer, style=style)
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_to_file({book_file: book, note_book_file: note_book})
            print(green("😊 Good bye!"))
            break
        elif command == "hello":
            print_with_random_help_msg()
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
        elif command == "delete-email":
            print(delete_email(args, book))
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
        elif command == "show-birthday":
            print(show_birthday(args, book))
            print_with_random_help_msg()
        elif command == "change-birthday":
            print(change_birthday(args, book))
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
        elif command == "change-note":
            print(change_note(args, note_book))
            print_with_random_help_msg()
        elif command == "delete-note":
            print(delete_note(args, note_book))
            print_with_random_help_msg()
        elif command == "find-note":
            print(find_note(args, note_book))
            print_with_random_help_msg()
        elif command == "all-notes":
            result_message = all_notes(note_book)
            if result_message:
                print(result_message)
            print_with_random_help_msg()
        elif command == "add-tag":
            result_message = add_tag(args, note_book)
            if result_message:
                print(result_message)
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
            result_message = search(args, book)
            if result_message:
                print(result_message)
            print_with_random_help_msg()
        elif command == "search-note":
            print(search_note(args, note_book))
            print_with_random_help_msg()
        else:
            print_with_random_emoji(red(" Invalid command."))
