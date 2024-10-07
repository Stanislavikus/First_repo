from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    # Отримуємо поточну дату
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        # Перетворюємо дату народження з рядка у об'єкт datetime
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        # Змінюємо рік дати народження на поточний рік
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже минув у цьому році, розглядаємо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Визначаємо кількість днів до дня народження
        days_until_birthday = (birthday_this_year - today).days

        # Перевіряємо, чи день народження випадає на наступні 7 днів
        if 0 <= days_until_birthday <= 7:
            # Якщо день народження припадає на вихідний (субота або неділя)
            if birthday_this_year.weekday() >= 5:  # 5 - субота, 6 - неділя
                # Переносимо дату привітання на наступний понеділок
                next_monday = birthday_this_year + timedelta(days=(7 - birthday_this_year.weekday()))
                congratulation_date = next_monday
            else:
                congratulation_date = birthday_this_year

            # Додаємо користувача та дату привітання до списку
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

# Приклад використання
users = [
    {"name": "John Doe", "birthday": "1985.10.07"},
    {"name": "Jane Smith", "birthday": "1990.10.08"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
