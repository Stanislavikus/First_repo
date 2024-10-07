from datetime import datetime

def get_days_from_today(date):
    try:
        # Перетворення рядка дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime
        given_date = datetime.strptime(date, '%Y-%m-%d').date()
        # Отримання поточної дати
        today_date = datetime.today().date()
        # Розрахунок різниці між поточною датою та заданою датою
        delta = today_date - given_date
        # Повернення різниці у днях як ціле число
        return delta.days
    except ValueError:
        return "Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'."
    # Виклик функції та виведення результату
print(get_days_from_today("2021-10-09"))