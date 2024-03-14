import os
import pickle
from src.classes.addressBook import AddressBook
from src.classes.noteBook import NoteBook

def factory(book: AddressBook | NoteBook, file_name) -> AddressBook | NoteBook:
    instance = None
    book_from_file = None
    if os.path.isfile(file_name):
        with open(file_name, 'rb') as file:
            book_from_file = pickle.load(file)
    if book_from_file:
        instance = book_from_file
    else:
        instance = book()
    return instance