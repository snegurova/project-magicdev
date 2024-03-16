from datetime import datetime
from .field import Field
from ..tools.colors import magenta

class Birthday(Field):
    def __init__(self, value):
        try:
            birthday = datetime.strptime(value, '%d.%m.%Y')
            super().__init__(birthday)
        except ValueError:
            raise ValueError(magenta("❗  Date format should be DD.MM.YYYY"))
        
    def __str__(self):
        return datetime.strftime(self.value, '%d.%m.%Y')
    
