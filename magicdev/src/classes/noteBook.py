from ..tools.colors import green
from .book import Book


class NoteBook(Book):
    def __str__(self):
        res = f"|{'Title':^15}|{'Description':<100}|{'#tags':^20}|\n|{'-'*15}|{'-'*100}|{'-'*20}|\n"
        for key, note in self.data.items():
            tags = "-----"
            if len(note.tags) > 0:
                tags = " #".join(p for p in note.tags)
            res += f"|{key:^15}|{note.description.value:<100}|{tags:^20}\n"
        return res

    def search_note(self, search_str):
        matches = self.search(search_str)
        res = green(f"😳 No results found by:\"{search_str}\" ")
        for _, record in self.data.items():
            tags = " ".join(p.lower() for p in record.tags)
            if search_str.lower() in tags:
                matches.append(record)
        if len(matches):
            res = f"|{'Title':^15}|{'Description':<100}|{'#tags':^20}|\n|{'-'*15}|{'-'*100}|{'-'*20}|\n"
            for match in matches:
                res += repr(match) + "\n"
        return res
