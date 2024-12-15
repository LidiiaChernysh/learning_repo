game_string = 'My favorite "Game"'

s = "Hello world!"
print(s[0])# H
print(s[-1])# !

s = "Hello world!"
#s[0] = "Q"# Тут буде викликано виняток (помилка) TypeError

###
s = "Hello" 
print(s.upper()) # Виведе 'HELLO'

###
s = "Some Text"
print(s.lower())  # Виведе 'some text'

###
s = "Bill Jons"
print(s.startswith("Bi"))  # Виведе True

###
s = "hello.jpg"
print(s.endswith("jpg"))  # Виведе True

###
s = "hello world".capitalize()  # Результат: "Hello world"
s = "hello world".title()  # Результат: "Hello World"

###
"123".isdigit()  # True
"hello".isalpha()  # True
" ".isspace()  # True


##################
# Просте форматування рядка
name = 'John'
print('Hello, {}!'.format(name))

# Форматування з декількома аргументами
age = 25
print('Hello, {}. You are {} years old.'.format(name, age))

# Використання іменованих аргументів
print('Hello, {name}. You are {age} years old.'.format(name='Jane', age=30))

# Використання індексів для вказівки порядку аргументів
print('Hello, {1}. You are {0} years old.'.format(age, name))

###
s = "Hello, World!"
first_five = s[:5]
print(first_five)  # Виведе 'Hello'

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = numbers[0:10:2]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = numbers[1:10:2]

even_numbers = numbers[1::2] # Виведе [2, 4, 6, 8, 10]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
three_numbers = numbers[2:10:3]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reverse_numbers = numbers[::-1]
print(reverse_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
copy_numbers = numbers[:]
print(copy_numbers)

