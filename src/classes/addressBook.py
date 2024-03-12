from collections import defaultdict
from datetime import datetime

from src.classes.book import Book


class AddressBook(Book):

    def __str__(self):
        res = f'|{'Name':^15}|{'Phone':<30}|{'Birthday':^15}|{'Address':<30}|\n'
        for key, record in self.data.items():
            phones = ", ".join((p.value for p in record.phones))
            birthday = datetime.strftime(record.birthday.value, '%d.%m.%Y') if record.birthday else "----"
            address = record.address.value if record.address else "----"
            res += f"|{key:^15}|{phones:<30}|{birthday:^15}|{address:<30}|\n"
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
