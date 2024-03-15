# Assistant Bot

Assistant Bot is a console-based application written in Python. It serves as a personal assistant for managing contacts and notes efficiently.

## Features

- Manage contacts: add, change, delete, search contacts
- Manage contact details: phone numbers, emails, addresses, birthdays
- Manage notes: add, change, delete notes, add tags
- View all contacts and notes
- Search contacts by various criteria

## Getting Started

1. Clone the repository:

git clone https://github.com/snegurova/project-magicdev.git

2. Navigate to the project directory:

cd project-magicdev

3. Install the required dependencies:

pip install -r requirements.txt

4. Run the application:

python main.py

## Installation Instructions for Windows

These instructions will guide you through the process of installing the bot on your Windows computer.

1. Open Terminal.

2. Type `cmd` to launch the Windows Command Prompt.

3. Enter the following command to create a Python virtual environment: `py -m venv <DIR>`
   
   *Replace `<DIR>` with the name of the folder where you want to save the virtual environment (e.g., env, vene, myenv, etc.).*

4. Once the virtual environment is created, activate it by entering the following command: `<DIR>\Scripts\activate`

5. Install 'pip' and 'setuptools' by running the following command:

    `py -m pip install pip setuptools`

6. Install the bot by running the following command:

    `py -m pip install -e .`

7. After successful installation, you can start the bot by entering the following command: `magicdev`

## Usage
The application accepts various commands to perform different actions. Here are the available commands:


| Command                                                                 | Description                                                             |
|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| <span style="color:blue">**hello**</span>                               | Say Hi to Bot and it will start work.                                   |
| <span style="color:blue">**help**</span>                                | List of all bot commands. You`re already here.                          |
| <span style="color:green">**add [name] [phone]**</span>                  | Add a new contact.                                                      |
| <span style="color:orange">**change [name] [old phone] [new phone]**</span> | Change contact information.                                           |
| <span style="color:blue">**phone [name]**</span>                         | Find phone number of a contact.                                         |
| <span style="color:green">**add-email [name] [email]**</span>            | Add email to a contact.                                                 |
| <span style="color:orange">**change-email [old email] [new email]**</span> | Change email of a contact.                                              |
| <span style="color:green">**add-birthday [name] [birthday-date]**</span>  | Add birthday to a contact.                                             |
| <span style="color:orange">**change-birthday [name] [new birthday]**</span> | Change birthday of a contact.                                          |
| <span style="color:orange">**show-birthday [name]**</span>               | Show birthday of a contact.                                             |
| <span style="color:blue">**birthdays [day]**</span>                      | Show birthdays within a range of days.                                  |
| <span style="color:green">**add-address [name] [address]**</span>        | Add address to a contact. Address argument should not contain spaces.   |
| <span style="color:orange">**change-address [name] [new address]**</span> | Change address of a contact.                                            |
| <span style="color:blue">**search [keyword]**</span>                     | Give back list of contacts by keyword (phone, name etc) with partial coincidence. |
| <span style="color:blue">**all**</span>                                  | Show all contacts.                                                      |
| <span style="color:red">**delete [name]**</span>                         | Delete a contacts.                                                      |
| <span style="color:green">**add-note [title]**</span>                     | Create a note.                                                          |
| <span style="color:orange">**change-note [title]**</span>                 | Change a note description.                                              |
| <span style="color:blue">**find-note [title]**</span>                     | Find a note by title.                                                   |
| <span style="color:blue">**search-note [keyword]**</span>                | Give back list of notes by keyword (tag or title) with partial coincidence. |
| <span style="color:red">**delete-note [title]**</span>                    | Delete a note.                                                          |
| <span style="color:blue">**all-notes**</span>                             | Show all Notes.                                                         |
| <span style="color:green">**add-tag [note-title]**</span>                 | Add a tag to a note.                                                    |
| <span style="color:red">**remove-tag [note-title]**</span>                | Remove tag from note.                                                   |
| <span style="color:blue">**close/exit**</span>                            | Close the program with saving data.                                      |


## License
This project is licensed under the MIT License - see the LICENSE file for details.