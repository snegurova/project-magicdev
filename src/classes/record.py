import re
from src.classes.birthday import Birthday
from src.classes.name import Name
from src.classes.phone import Phone
from src.classes.address import PostalAddress


class Record:
    def __init__(self, name, address = None, birthday = None):
        self.name = Name(name)
        self.phones = []
        if address:
            self.address = PostalAddress(address)
        else:
            self.address = None
        if birthday:
            self.birthday = Birthday(birthday)
        else:
            self.birthday = None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

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

    def add_postal_address(self, address):
        """adds address to record"""
        self.address = PostalAddress(address)

    def edit_postal_address(self, new_address):
        """edits address in record"""
        self.address = PostalAddress(new_address)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def __repr__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
