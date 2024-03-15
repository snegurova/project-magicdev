

def display_commands():
    commands = [
        {"Command": "hello", "Description": "Say Hi to Bot and it will start work."},
        {"Command": "help", "Description": "List of all bot commands. You`re already here."},
        {"Command": "add [name] [phone]", "Description": "Add a new contact."},
        {"Command": "change [name] [old phone] [new phone]", "Description": "Change contact information."},
        {"Command": "phone [name]", "Description": "Find phone number of a contact."},
        {"Command": "add-email [name] [email]", "Description": "Add email to a contact."},
        {"Command": "change-email [old email] [new email]", "Description": "Change email of a contact."},
        {"Command": "add-birthday [name] [birthday-date]", "Description": "Add birthday to a contact."},
        {"Command": "show-birthday [name]", "Description": "Show birthday of a contact."},
        {"Command": "birthdays [day]", "Description": "Show birthdays within a range of days."},
        {"Command": "add-address [name] [address]", "Description": "Add address to a contact. Address argument should not contain spaces."},
        {"Command": "change-address [name] [new address]", "Description": "Change address of a contact."},
        {"Command": "search [name]", "Description": "Search for a contact."},
        {"Command": "all", "Description": "Show all contacts."},
        {"Command": "delete [name]", "Description": "Delete a contacts."},
        {"Command": "add-note [title]", "Description": "Create a note."},
        {"Command": "change-note [title]", "Description": "Change a note description."},
        {"Command": "delete-note [title]", "Description": "Delete a note."},
        {"Command": "all-notes", "Description": "Show all Notes."},
        {"Command": "add-tag [note-title]", "Description": "Add a tag to a note."},
        {"Command": "remove-tag [note-title]", "Description": "Remove tag from note."},
        {"Command": "close/exit", "Description": "Close the program with saving data."},
    ]

    max_command_len = max(len(command["Command"]) for command in commands)
    max_description_len = max(len(command["Description"]) for command in commands)

    print(f"| {'Command':<{max_command_len}} | {'Description':<{max_description_len}} |")
    print(f"|{'-' * (max_command_len + 2)}|{'-' * (max_description_len + 2)}|")
    for command in commands:
        print(f"| {command['Command']:<{max_command_len}} | {command['Description']:<{max_description_len}} |")