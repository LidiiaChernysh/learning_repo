def print_max(a: int, b: int):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'дорівнює', b)
    else:
        print(b, 'максимально')

print_max(3, 4)  # пряма передача значень

x = 5
y = 7
print_max(x, y)  # передача змінних у якості аргументів



def add_numbers(num1: int, num2: int) -> int:
    sum = num1 + num2
    return sum

result = add_numbers(5, 10)
print(result)  # Виведе: 15



def greet(name: str) -> str:
    return f"Привіт, {name}!"

greeting = greet("Lidiia")
print(greeting)  # Виведе: Привіт, Lidiia!



def is_even(num: int) -> bool:
    return num % 2 == 0

check_even = is_even(4)
print(check_even)  # Виведе: True



#!!!!!!!!!!!!!!! Незмінні типи в Python — це ті, що не можуть бути змінені після їх створення. 
# Це включає типи, як-от цілі числа int, дійсні числа float, рядки str, кортежі tuple.
#
#  Коли незмінний об'єкт передається у функцію, фактично передається його копія, 
# і будь-які зміни цього об'єкту в функції не впливають на оригінальний об'єкт.

def modify_string(original: str) -> str:
    original = "змінено"
    return original

str_var = "оригінал"
print(modify_string(str_var))  # виведе: змінено
print(str_var)                # виведе: оригінал


#У цьому прикладі, навіть після зміни рядка в функції modify_string, 
# оригінальна змінна str_var залишається незмінною.
# 
# Змінні типи, як списки list, словники dict, множини set, можуть змінюватися. 
# Коли змінний об'єкт передається у функцію, передається посилання на цей об'єкт, 
# і зміни, зроблені всередині функції, відображаються на оригінальному об'єкті.

def modify_list(lst: list) -> None:
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # виведе: [1, 2, 3, 4]


def modify_list(lst: list) -> None:
    lst = lst.copy()
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # виведе: [1, 2, 3]


def invite_to_event(username):
    print(f"Dear {username}, we have the honour to invite you to our event")

username = "Vasya"
invite_to_event( username)



def outer_func():
    enclosing_var = "Я змінна в функції, що охоплює"

    def inner_func():
        print("Всередині вкладеної функції:", enclosing_var)

    inner_func()

outer_func()



# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! NON LOCAL !!!!!!!!!!!!!!!!!!!
# Коли ми перебуваємо всередині функції func_inner, змінна x, визначена у першому рядку функції 
# func_outer, знаходиться в enclosing області видимості для неї. 
# Якщо ми захочемо використати саме цю змінну x, ми повинні оголосити її nonlocal x
#  всередині функції func_inner. Це означає, що змінна x, яку вона буде змінювати, 
# є не локальною для func_inner, а знаходиться на більш високому рівні — в нашому випадку, 
# в func_outer. Тому, коли func_inner змінює x на 5, ця зміна відображається на x в func_outer.

def func_outer():
    x = 2

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    return x

result = print(func_outer())  # 5

x = 50

def func():
    global x
    print('x дорівнює', x)  # x дорівнює 50
    x = 2
    print('Змінюємо глобальне значення x на', x)  # Змінюємо глобальне значення x на 2

func()
print('Значення x складає', x)# Значення x складає 2


def real_cost(base: int, discount: float = 0) -> float:
    return base * (1 - discount)



##### args, kwargs #########

def concatenate(*args) -> str:
    result = ""
    for arg in args:
        result += arg
    return result

print(concatenate("Hello", " ", "world", "!"))

def concatenate(*strings) -> str:
    result = ""
    for arg in strings:
        result += arg
    return result

print(concatenate("Hello", " ", "world", "!"))



def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Alice", age=25)

def example_function(*args, **kwargs):
    print("Позиційні аргументи:", args)
    print("Ключові аргументи:", kwargs)

example_function(1, 2, 3, name="Alice", age=25)



def discount_price(price: float, discount: float) -> float: 
    def apply_discount():
        nonlocal price
        return price * (1 - discount)
    
    price = apply_discount()

    return price
print(discount_price(100, 0.08))


def get_fullname(first_name: str, last_name: str, middle_name="") -> str:

    if len(middle_name.replace(" ", "")) != 0:
        result = f"{first_name} {middle_name} {last_name}"
        return result
    else:
        result = f"{first_name} {last_name}"
        return result

print(get_fullname("Lidiia", "Chernysh", "test"))