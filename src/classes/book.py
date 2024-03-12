from collections import UserDict

from src.classes.record import Record
from src.classes.note import Note


class Book(UserDict):
    def add_record(self, record: Record | Note):
        self.data.__setitem__(record.name.value, record)

    def find(self, name) -> Record | Note | None:
        if name in self.data:
            return self.data[name]
        return None
    
    def delete(self, name, message):
        self.__delitem__(name)
        print(message)