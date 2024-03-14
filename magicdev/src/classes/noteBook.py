from .book import Book

class NoteBook(Book):
    def __str__(self):
        res = f"|{'Title':^15}|{'Description':<100}|\n|{'-'*15}|{'-'*100}|{'-'*20}|\n"
        for key, note in self.data.items():
            tags = ' #'.join(p.value for p in note.tags) if hasattr(note, 'tags') and isinstance(note.tags, (list, tuple)) else '-----'
            res += f"|{key:^15}|{note.description.value:<100}|{tags:^20}\n"
        return res
    
    def search_note(self, seach_str):
        matches = self.search(seach_str)
        if(len(matches)):
            print(f"|{'Note':^15}|{'Description':<100}|{'Tags':^20}")
            for match in matches:
                print(repr(match))