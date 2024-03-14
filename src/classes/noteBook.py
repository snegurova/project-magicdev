from src.classes.book import Book

class NoteBook(Book):
    def __str__(self):
        res = f"|{'Title':^15}|{'Description':<100}|\n|{"-"*15}|{"-"*100}|{"-"*20}|\n"
        for key, note in self.data.items():
            tags = " #" + " #".join(note.tags) if note.tags else "-----"
            res += f"|{key:^15}|{note.description.value:<100}|{tags:^20}\n"
        return res

