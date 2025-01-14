import time

"""

Метод time.time() повертає поточний час у секундах з 1 січня 1970 року (epoch time).

"""

current_time = time.time()
print(f"Поточний час: {current_time}")


# Метод time.sleep(seconds) зупиняє виконання програми на вказану кількість секунд. 
# Наприклад цей код зупиняє виконання програми на 5 секунд.

print("Початок паузи")
# time.sleep(5)
print("Кінець паузи")


######## Метод time.ctime([seconds]) перетворює часову мітку (кількість секунд)
#  у зрозуміле для людини текстове представлення. 
# Якщо аргумент не вказаний, використовується поточний час.


current_time = time.time()
print(f"Поточний час: {current_time}")

readable_time = time.ctime(current_time)
print(f"Читабельний час: {readable_time}")


#####
import time

current_time = time.time()
print(f"Поточний час: {current_time}")

local_time = time.localtime(current_time)
print(f"Місцевий час: {local_time}")





### Досить важливим є метод time.perf_counter(), 
# який надає доступ до лічильника з високою точністю, 
# та є ідеальним для вимірювання коротких інтервалів часу.

# використаємо time.perf_counter() для вимірювання часу виконання деякого блоку коду:

# Записуємо час на початку виконання
start_time = time.perf_counter()

# Виконуємо якусь операцію
for _ in range(1_000_000):
    pass  # Просто проходить цикл мільйон разів

# Записуємо час після виконання операції
end_time = time.perf_counter()

# Розраховуємо та виводимо час виконання
execution_time = end_time - start_time
print(f"Час виконання: {execution_time} секунд")



# Один мільйон
a = 1_000_000
print(a)  # Виведе 1000000

# Десять мільйонів
b = 10_000_000
print(b)  # Виведе 10000000

# Один мільярд
c = 1_000_000_000
print(c)  # Виведе 1000000000


"""
Ключові аспекти: основні методи модуля time в Python


time.time(): Повертає поточний час у секундах з 1 січня 1970 року (epoch time).
time.sleep(seconds): Зупиняє виконання програми на вказану кількість секунд.
time.ctime([seconds]): Перетворює часову мітку в текстове представлення, зрозуміле для людини.
time.localtime([seconds]): Перетворює часову мітку в структуру struct_time у місцевій часовій зоні.
time.gmtime([seconds]): Аналогічно localtime, але повертає struct_time у форматі UTC.
time.perf_counter(): Повертає лічильник з високою точністю для вимірювання коротких інтервалів часу.

"""


