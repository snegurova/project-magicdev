from collections import defaultdict
from datetime import datetime

from src.classes.book import Book


class AddressBook(Book):

    def __str__(self):
        res = f"|{'Name':^15}|{'Phone':<30}|{'Birthday':^15}|{'Address':<30}|\n"
        for key, record in self.data.items():
            phones = ", ".join((p.value for p in record.phones))
            birthday = datetime.strftime(record.birthday.value, '%d.%m.%Y') if record.birthday else "----"
            address = record.address.value if record.address else "----"
            res += f"|{key:^15}|{phones:<30}|{birthday:^15}|{address:<30}|\n"
        return res
    
    def get_birthdays_per_days(self, days):
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
            is_birthday_next_year = (birthday_this_year < today) or (birthday_this_year < today.replace(day = today.day - 2))
            if is_birthday_next_year:
                birthday_this_year = birthday.replace(year = today.year + 1)
            
            delta_start = 0
            delta_end = int(days)
            delta_days = (birthday_this_year - today).days
            if delta_days > delta_start and delta_days < delta_end:
                str_day_of_week = (birthday_this_year.strftime('%A'), datetime.strftime(birthday_this_year, '%d.%m.%Y'))
                birthdays_per_week[str_day_of_week].append(name)
        for day, users in birthdays_per_week.items():
            print(f"{day[0]:^15} | {day[1]:^12} | {', '.join(users):^15}")
            
    def search(self, seach_str):
        matches = []
        for record in self.data.values():
            if seach_str.lower() in record.name.value.lower():
                matches.append(record)
        if(len(matches)):
            print(f'|{"Name":^15}|{"Phones":^25}|{"Birthday":^15}|{"Address":^25}|{"Email":^25}|')
            for match in matches:
                print(repr(match))
            