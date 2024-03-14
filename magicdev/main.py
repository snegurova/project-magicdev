from pathlib import Path
from .src.bot import bot

def main():
    NOTE_BOOK_PATH = Path(__file__).parents[1] / "book.bin"
    ADDRESS_BOOK_PATH = Path(__file__).parents[1] / "note-book.bin"
    bot(ADDRESS_BOOK_PATH, NOTE_BOOK_PATH)

if __name__ == "__main__":
    main()