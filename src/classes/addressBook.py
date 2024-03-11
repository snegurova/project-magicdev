from collections import UserDict, defaultdict
from datetime import datetime

from src.classes.record import Record


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data.__setitem__(record.name.value, record)

    def find(self, name) -> Record | None:
        if name in self.data:
            return self.data[name]
        return None
    
    def delete(self, name):
        self.__delitem__(name)
        print(f"Contact {name} was deleted")

    def __str__(self):
        res = f'|{'Name':^15}|{'Phone':<30}|{'Birthday':^15}|\n'
        for key, record in self.data.items():
            phones = ", ".join((p.value for p in record.phones))
            birthday = datetime.strftime(record.birthday.value, '%d.%m.%Y') if record.birthday else "----"
            res += f"|{key:^15}|{phones:<30}|{birthday:^15}|\n"
        return res
    
    def get_birthdays_per_week(self):
        users = []
        for user in self.data.values():
            if user.birthday:
                users.append({"name": user.name.value, "birthday": user.birthday.value})
        birthdays_per_week = defaultdict(list)
        today = datetime.today().date()
        for user in users:
            name = user["name"]
            birthday = user["birthday"].date()
            birthday_this_year = birthday.replace(year = today.year)
            is_monday = today.weekday() == 0
            is_birthday_next_year = (not is_monday and birthday_this_year < today) or (is_monday and birthday_this_year < today.replace(day = today.day - 2))
            if is_birthday_next_year:
                birthday_this_year = birthday.replace(year = today.year + 1)
            
            delta_start = 0
            delta_end = 7
            if is_monday:
                delta_start = -2
                delta_end = 5
            delta_days = (birthday_this_year - today).days
            if delta_days > delta_start and delta_days < delta_end:
                str_day_of_week = birthday_this_year.strftime('%A')
                if str_day_of_week in ['Saturday', 'Sunday']:
                    str_day_of_week = 'Monday'
                birthdays_per_week[str_day_of_week].append(name)
        for day, users in birthdays_per_week.items():
            print(f"{day}: {', '.join(users)}")




if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    print(book)
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

    print(book)