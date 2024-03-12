import re
from src.classes.birthday import Birthday
from src.classes.name import Name
from src.classes.phone import Phone
from src.classes.emailAddress import EmailAddress


class Record:
    def __init__(self, name, birthday = None):
        self.name = Name(name)
        self.phones = []
        self.emails = []
        if birthday:
            self.birthday = Birthday(birthday)
        else:
            self.birthday = None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def add_email(self, email):
        self.emails.append(EmailAddress(email))

    def change_email(self, email_to_find, new_email):
        pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if not re.match(pattern, email_to_find):
            raise ValueError("Please use correct e-mail address format. Example: 'ira@gmail.com', 'A111@ukr.net'")
        if not re.match(pattern, new_email):
            raise ValueError("Please use correct new e-mail address format. Example: 'ira@gmail.com', 'A111@ukr.net'")
        is_changed = False
        for email in self.emails:
            if email.value == email_to_find:
                email.value = new_email
                is_changed = True
                break
        if not is_changed:
            raise ValueError(f"Email '{email_to_find}' for contact '{self.name}' not found.")

    def add_phone(self, phone):
        for item in self.phones:
            if item.value == phone:
                raise ValueError("This phone already exists")
        phone_field = Phone(phone)
        self.phones.append(phone_field)

    def remove_phone(self, phone_to_delete):
        for phone in self.phones:
            if phone.value == phone_to_delete:
                self.phones.remove(phone)

    def edit_phone(self, phone_to_change, new_phone):
        if not (len(new_phone) == 10 and re.search(r'^([\s\d]+)$', new_phone)):
            raise ValueError("Error. Phone number should contain 10 numbers. Please enter correct number")
        is_changed = False
        for phone in self.phones:
            if phone.value == phone_to_change:
                phone.value = new_phone
                is_changed = True
        if not is_changed:
            raise ValueError(f"For contact {self.name} {phone_to_change} is not found")

    def find_phone(self, phone_to_find):
        for phone in self.phones:
            if phone.value == phone_to_find:
                return f"{phone_to_find} exists"
        return f"{phone_to_find} have not been added yet"

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def __repr__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
