
import re
from .field import Field

class EmailAddress(Field):
    def __init__(self, email):
        pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if re.match(pattern, email) is not None:
            super().__init__(email)
        else:
            raise ValueError("❗  Please use correct e-mail address format. Example: 'ira@gmail.com', 'A111@ukr.net'")
        
