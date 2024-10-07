import random

def get_numbers_ticket(min, max, quantity):
    # Перевірка, що параметри відповідають заданим обмеженням
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []
    
    # Генерація унікальних випадкових чисел
    numbers = random.sample(range(min, max + 1), quantity)
    
    # Сортування списку чисел
    numbers.sort()
    
    return numbers

# Приклад використання
print(get_numbers_ticket(1, 49, 6))  # Наприклад, [3, 15, 22, 28, 35, 47]