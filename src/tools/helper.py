

def display_commands():
    commands = [
        {"Command": "hello", "Description": "Say Hi to Bot and it will start work.", "Example": "Enter [hello]"},
        {"Command": "help", "Description": "List of all bot commands. You`re already here.", "Example": "Enter [help]"},
        {"Command": "add", "Description": "Add a new contact.", "Example": "Enter [add] [name] [phone]"},
        {"Command": "change", "Description": "Change contact information.", "Example": "Enter [change] [name] [old phone] [new phone]"},
        {"Command": "phone", "Description": "Find phone number of a contact.", "Example": "Enter [phone] [name]"},
        {"Command": "add-email", "Description": "Add email to a contact.", "Example": "Enter [add-email] [name] [email]"},
        {"Command": "change-email", "Description": "Change email of a contact.", "Example": "Enter [change-email] [old email] [new email]"},
        {"Command": "add-birthday", "Description": "Add birthday to a contact.", "Example": "Enter [add-birthday] [name] [birthday date]"},
        {"Command": "show-birthday", "Description": "Show birthdays.", "Example": "Enter [show-birthday] [name]"},
        {"Command": "birthdays", "Description": "Show birthdays within a range of days.", "Example": "Enter [birthdays]"},
        {"Command": "add-address", "Description": "Add address to a contact.", "Example": "Enter [add-address] [name]"},
        {"Command": "change-address", "Description": "Change address of a contact.", "Example": "Enter [change-address] [name]"},
        {"Command": "search", "Description": "Search for a contact.", "Example": "Enter [search] [name]"},
        {"Command": "all", "Description": "Show all contacts.", "Example": "Enter [all]"},
        {"Command": "delete", "Description": "Delete all contacts.", "Example": "Enter [delete] [name]"},
        {"Command": "add-note", "Description": "Create a note.", "Example": "Enter [add-note] [title]"},
        {"Command": "change-note", "Description": "Change a note description.", "Example": "Enter [change-note] [title]"},
        {"Command": "delete-note", "Description": "Delete a note.", "Example": "Enter [delete-note] [title]"},
        {"Command": "all-notes", "Description": "Show all Notes.", "Example": "Enter [all-notes]"},
        {"Command": "add-tag", "Description": "Add a tag to a note.", "Example": "Enter [add-tag] [title]"},
        {"Command": "remove_tag", "Description": "Remove tag from note.", "Example": "Enter [remove_tag] [title]"},
        {"Command": "close/exit", "Description": "Close the program with saving data.", "Example": "Enter [close] or [exit]"},
    ]

    max_command_len = max(len(command["Command"]) for command in commands)
    max_description_len = max(len(command["Description"]) for command in commands)
    max_example_len = max(len(command.get("Example", "")) for command in commands)

    print(f"| {'Command':<{max_command_len}} | {'Description':<{max_description_len}} | {'Example':<{max_example_len}} |")
    print(f"|{'-' * (max_command_len + 2)}|{'-' * (max_description_len + 2)}|{'-' * (max_example_len + 2)}|")
    for command in commands:
        example = command.get("Example", "")
        print(f"| {command['Command']:<{max_command_len}} | {command['Description']:<{max_description_len}} | {example:<{max_example_len}} |")