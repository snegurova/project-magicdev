import re
from .birthday import Birthday
from .name import Name
from .phone import Phone
from .address import PostalAddress
from .emailAddress import EmailAddress
from ..tools.colors import magenta, yellow, dark_green

class Record:
    def __init__(self, name, address = None, birthday = None):
        self.name = Name(name)
        self.phones = []
        if address:
            self.address = PostalAddress(address)
        else:
            self.address = None
        self.emails = []
        if birthday:
            self.birthday = Birthday(birthday)
        else:
            self.birthday = None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def change_birthday(self, new_birthday):
        if not re.match(r'^\d{2}\.\d{2}\.\d{4}$', new_birthday):
            raise ValueError(magenta("Incorrect date format. Use the format DD.MM.YYYY"))
        self.birthday = Birthday(new_birthday)

    def add_email(self, email):
        for item in self.emails:
            if item.value == email:
                raise ValueError(magenta(f"❗ {email} already exists."))
        self.emails.append(EmailAddress(email))

    def change_email(self, email_to_find, new_email):
        pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if not re.match(pattern, email_to_find):
            raise ValueError(magenta("❗  Please use correct e-mail address format. Example: 'ira@gmail.com', 'A111@ukr.net'"))
        if not re.match(pattern, new_email):
            raise ValueError(magenta("❗  Please use correct new e-mail address format. Example: 'ira@gmail.com', 'A111@ukr.net'"))
        is_changed = False
        for email in self.emails:
            if email.value == email_to_find:
                email.value = new_email
                is_changed = True
                break
        if not is_changed:
            raise ValueError(yellow(f"😳  Email '{email_to_find}' for contact '{self.name}' not found."))

    def add_phone(self, phone):
        for item in self.phones:
            if item.value == phone:
                raise ValueError(yellow("😳  This phone already exists"))
        phone_field = Phone(phone)
        self.phones.append(phone_field)

    def remove_phone(self, phone_to_delete):
        for phone in self.phones:
            if phone.value == phone_to_delete:
                self.phones.remove(phone)

    def edit_phone(self, phone_to_change, new_phone):
        if not (len(new_phone) == 10 and re.search(r'^([\s\d]+)$', new_phone)):
            raise ValueError(magenta("❗  Error. Phone number should contain 10 numbers. Please enter correct number"))
        is_changed = False
        for phone in self.phones:
            if phone.value == phone_to_change:
                phone.value = new_phone
                is_changed = True
        if not is_changed:
            raise ValueError(yellow(f"😳  For contact {self.name} {phone_to_change} is not found"))

    def find_phone(self, phone_to_find):
        for phone in self.phones:
            if phone.value == phone_to_find:
                return f"✌️ {phone_to_find} exists"
        return yellow(f"😳 {phone_to_find} have not been added yet")

    def add_postal_address(self, address):
        """adds address to record"""
        self.address = PostalAddress(address)

    def edit_postal_address(self, new_address):
        """edits address in record"""
        self.address = PostalAddress(new_address)

    def __str__(self):
        return dark_green(f"✌️ Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}")

    def __repr__(self):
        address_str = self.address.value if self.address is not None else yellow("🫤 No address")
        birthday_str = str(self.birthday) if self.birthday is not None else yellow("🫤 Not indicated")
        emails_str = '; '.join(p.value for p in self.emails) if self.emails else yellow("🫤 No emails")
        return f"|{self.name.value:^15}|{'; '.join(p.value for p in self.phones):^25}|{birthday_str:^15}|{address_str:^25}|{emails_str:^25}|"
