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

##############
odd_numbers = [1, 3, 5, 7, 9]
for i in odd_numbers:
    print(i ** 2)

####
k = 0
while k < 10:
    k = k + 1
    print(k)

###
a = 0
while True:
    print(a)
    if a >= 20:
        break
    a = a + 1

while True:
    user_input = input()
    print(user_input)
    if user_input == "exit":
        break
"""

a = 0
while a < 6:
    a = a + 1
    if not a % 2:
        continue
    print(a)

print(not 3 % 2)

while True:
    number = input("number = ")
    number = int(number)
    while True:
        print(number)
        number = number - 1
        if number < 0:
            break

########
some_list = ["apple", "banana", "cherry"]
for index, value in enumerate(some_list):
    print(index, value)

#####
list1 = ["зелене", "стигла", "червоний"]
list2 = ["яблуко", "вишня", "томат"]
for number, letter in zip(list1, list2):
    print(number, letter)

#####
for key in numbers.keys():
    print(key)

for val in numbers.values():
    print(val)

for key, value in numbers.items():
    print(key, value)
