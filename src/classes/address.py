from src.classes.field import Field

# Add validation - length from 1 to 255, otherwise raise Value error with message
class PostalAddress(Field):
    def __init__(self, address):
        if 0 < len(address) <= 255:
            super().__init__(address)
        else:
            raise ValueError(
                "Error. Address can contain maximum 255 symbols. Please enter correct Address"
            )
