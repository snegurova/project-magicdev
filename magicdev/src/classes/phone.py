import re
from .field import Field
from ..tools.colors import magenta

class Phone(Field):
    def __init__(self, phone):
        if len(phone) == 10 and re.search(r'^([\s\d]+)$', phone):
            super().__init__(phone)
        else:
            raise ValueError(magenta("❗  Error. Phone number should contain 10 numbers. Please enter correct number"))
