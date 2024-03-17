from collections import UserDict

from .record import Record
from .note import Note


class Book(UserDict):
    def add_record(self, record: Record | Note):
        self.data.__setitem__(record.name.value, record)

    def find(self, name) -> Record | Note | None:
        if name in self.data:
            return self.data[name]
        return None

    def delete(self, name):
        self.__delitem__(name)

    def search(self, search_str):
        matches = []
        sorted_dict = dict(sorted(self.data.items()))
        for record in sorted_dict.values():
            if search_str.lower() in record.name.value.lower():
                matches.append(record)
        return matches
