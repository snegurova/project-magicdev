from src.classes.name import Name
from src.classes.description import Description
from src.classes.tag import Tag


class Note:
    def __init__(self, title, description):
        self.name = Name(title)
        self.description = Description(description)
        self.tags = set()

    def change_description(self, description):
        self.description = Description(description)

    def add_tag(self, tag):
        """adds tag to note"""
        new_tag = Tag(tag)
        if new_tag.value in self.tags:
            raise ValueError(f"Tag #{tag} already exists")
        self.tags.add(new_tag.value)

    def remove_tag(self, tag_to_remove):
        """removes tag from note"""
        self.tags.discard(tag_to_remove)
        
    def __repr__(self):
        return f"Note: {self.name.value}, description: {self.description.value}, tags: # {' #'.join(p.value for p in self.tags)}"
