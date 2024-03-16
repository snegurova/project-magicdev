from .field import Field
from ..tools.colors import magenta


class Description(Field):
    def __init__(self, description):
        if len(description) > 0 and len(description) <= 255:
            super().__init__(description)
        else: raise ValueError(magenta("❗  Description should be between 0 to 255 characters"))