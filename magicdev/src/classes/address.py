from .field import Field
from ..tools.colors import magenta

class PostalAddress(Field):
    def __init__(self, address):
        if 0 < len(address) <= 255:
            super().__init__(address)
        else:
            raise ValueError(
                magenta("❗ Error. Address can contain maximum 255 symbols. Please enter correct Address")
            )
