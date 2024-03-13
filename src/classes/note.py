from src.classes.name import Name
from src.classes.description import Description


class Note:
    def __init__(self, title, description):
        self.name = Name(title)
        self.description = Description(description)

    def change_description(self, description):
        self.description = Description(description)

    def __repr__(self):
        return f"Note: {self.name.value}, description: {self.description.value}"