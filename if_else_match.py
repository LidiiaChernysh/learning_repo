some_data = None
if some_data:
    msg = some_data
else:
    msg = "Не було повернено даних"

#### match
"""
match змінна:
    case шаблон1:
        # виконати код для шаблону 1
    case шаблон2:
        # виконати код для шаблону 2
    case _:
        # виконати код, якщо не знайдено відповідностей

Цей оператор був введений для випадків, коли нам потрібно виконати різні дії в залежності 
від значення однієї змінної, особливо коли таких варіантів багато. 
Раніше для цього ми використовували довгий ланцюжок if-elif-else, 
але тепер оператор match робить код чистішим та простішим для розуміння.
"""


fruit = "apple"

match fruit:
    case "apple":
        print("This is an apple.")
    case "banana":
        print("This is a banana.")
    case "orange":
        print("This is an orange.")
    case _:
        print("Unknown fruit.")

point = (1, 0)

match point:
    case (0, 0):
        print("Точка в центрі координат")  
    case (0, y):
        print(f"Точка лежить на осі Y: y={y}")  
    case (x, 0):
        print(f"Точка лежить на осі X: x={x}") 
    case (x, y):
        print(f"Точка має координати:  x={x}, y={y}") 
    case _:
        print("Це не точка")

# 3нак _ в шаблоні використовується як "заповнювач", що означає "будь-яке інше значення".

pets = ["dog", "fish", "cat"]

match pets:
    case ["dog", "cat", _]:
        # Випадок, коли є і собака, і кіт
        print("There's a dog and a cat.")
    case ["dog", _, _]:
        # Випадок, коли є тільки собака
        print("There's a dog.")
    case _:
        # Випадок для інших комбінацій
        print("No dogs.")



# Тернарні операції
is_nice = True
state = "nice" if is_nice else "not nice"

some_data = None
msg = some_data or "Не було повернено даних"

if 5 > 2: print("Пять больше, чем два!")

