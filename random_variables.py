import random

"""
Для отримання випадкового цілого числа з рівномірного розподілу 
в інтервалі між a та b включно треба використати метод random.randint(a, b). 
Він повертає випадкове ціле число N таке, що a <= N <= b:
"""

dice_roll = random.randint(1, 6)
print(f"Ви кинули {dice_roll}")



#Метод random.random() потрібен, щоб отримати випадкове число в інтервалі 0, 1. 
# Він генерує випадкове дійсне число між 0.0 (включно) та 1.0 (не включно):
num = random.random()
print(num)


# Тут в f рядку з'явилось форматування {fill_percentage:.2f} яке вказує, 
# яким чином відображати змінну fill_percentage.
#  Вираз .2 це кількість знаків після десяткової крапки. 
# У цьому випадку вказано, що потрібно відображати два знаки для дійсного числа. 
# Символ f означає, що число має бути відображене у форматі дійсного числа.
fill_percentage = random.random() * 100
print(f"Заповнення: {fill_percentage:.2f}%")


print(random.randrange(10))  # Верхня межа є 10, але не включається


cards = ["Туз", "Король", "Дама", "Валет", "10", "9", "8", "7", "6"]
random.shuffle(cards)
print(f"Перемішана колода: {cards}")



fruits = ['apple', 'banana', 'orange']
print(random.choice(fruits))



numbers = [1, 2, 3, 4, 5]
chosen_numbers = random.choices(numbers, k=3)
print(chosen_numbers)



colors = ['червоний', 'зелений', 'синій']
weights = [10, 1, 1] # Елемент 'червоний' має набагато більшу ймовірність бути обраним
chosen_color = random.choices(colors, weights, k=1)
print(chosen_color)  


# Якщо виникає необхідність вибрати N елементів зі списку і вони при цьому не повторювалися 
# треба використати метод random.sample(population, k). 
# Він повертає список довжиною k з унікальними елементами, вибраними випадково з population.

participants = ['Анна', 'Богдан', 'Віктор', 'Галина', 'Дмитро', 'Олена', 'Женя', 'Зорян', 'Ігор', 'Йосип']
team = random.sample(participants, 4)
print(f"Команда: {team}")



price = random.uniform(50, 100)
print(f"Випадкова ціна: {price:.2f}")


"""
Ключові аспекти: методи для роботи з випадковими величинами


random.randint(a, b): Отримання випадкового цілого числа з рівномірного розподілу в інтервалі між a та b включно.
random.random(): Отримання випадкового числа в інтервалі між 0.0 (включно) та 1.0 (не включно).
random.randrange(start, stop[, step]): Отримання випадкового числа з заданого діапазону, з можливістю вказати крок між значеннями.
random.shuffle(x): Перемішування порядку елементів у списку x.
random.choice(seq): Вибір випадкового елемента з послідовності seq (списку або кортежу).
random.choices(population, weights=None, cum_weights=None, k=1): Генерація випадкової вибірки з можливістю зазначити ймовірності для кожного елемента та повторення у вибірці.
random.sample(population, k): Отримання унікальних випадкових елементів зі списку population довжиною k.
random.uniform(a, b): Отримання випадкового дійсного числа N такого, що a <= N <= b.
"""