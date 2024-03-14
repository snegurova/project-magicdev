from .field import Field

class PostalAddress(Field):
    def __init__(self, address):
        if 0 < len(address) <= 255:
            super().__init__(address)
        else:
            raise ValueError(
                "Error. Address can contain maximum 255 symbols. Please enter correct Address"
            )
