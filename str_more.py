"""
Щоб структурувати код і не додавати зайвих перенесень, 
ви можете розбити одну рядкову змінну на декілька частин:
"""
one_line_text = "Textual data in Python is handled with str objects," \
                " or strings. Strings are immutable sequences of Unicode" \
                " code points. String literals are written in a variety " \
                " of ways: single quotes, double quotes, triple quoted."

# Зверніть увагу на символ \ в кінці першого та другого рядка коду, 
# він вказує інтерпретатору ігнорувати закінчення рядка і продовжити відразу з наступного.



# У Python, коли ви поміщаєте два рядкових літерали поруч, 
# вони автоматично конкатенуються (об'єднуються в один рядок). 
# Це відомо як неявна конкатенація рядків:
("spam " "eggs") == "spam eggs"  # True


#Ця особливість часто використовується для зручності, 
# особливо при написанні довгих рядків і тому 
# змінну one_line_text можна записати наступним чином.
one_line_text = ("Textual data in Python is handled with str objects,"
                " or strings. Strings are immutable sequences of Unicode"
                " code points. String literals are written in a variety "
                " of ways: single quotes, double quotes, triple quoted.")

query = ("SELECT * "
         "FROM some_table "
         "WHERE condition1 = True "
         "AND condition2 = False")


print("Hello\nWorld")
print("Hello\tWorld")

#Приклад для повернення каретки \r (carriage return). 
print("Hello my little\rsister")
# Виведення відбувається наступним чином: коли ми зустрічаємо символ \r, 
# то повертаємося на початок рядка і продовжуємо виведення. 
# Це перезаписує попередній вивід:  sistermy little



print("Hello\bWorld")
print("Hello\\World")

# Щоб екранувати одинарні та подвійні лапки та дозволити використовувати лапки всередині рядкових літералів.
print('It\'s a beautiful day')
print("He said, \"Hello\"")


# find
s = "Hi there!"

start = 0
end = 7

print(s.find("er", start, end)) # 5
print(s.find("q")) # -1


s = 'Some words'

print(s.find("o")) # 1
print(s.rfind('o')) # 6


print(s.index("o")) # 1
print(s.rindex('o')) # 6


# split() str.split(separator=None, maxsplit=-1)

text = "hello world"
result = text.split()
print(result)  # Виведе: ['hello', 'world']

text = "apple,banana,cherry"
result = text.split(',')
print(result)  # Виведе: ['apple', 'banana', 'cherry']


# join()  string.join(iterable)
list_of_strings = ['Hello', 'world']
result = ' '.join(list_of_strings)
print(result)  # Виведе: 'Hello world'

elements = ['earth', 'air', 'fire', 'water']
result = ', '.join(elements)
print(result)  # Виведе: 'earth, air, fire, water'


# strip()
clean = '   spacious   '.strip()
print(clean) # spacious


# str.replace(old, new, count=-1)
"""
Загалом метод replace() широко використовується для обробки тексту в Python.
Та може бути корисним коли необхідно:

Виправлення помилок у тексті
Заміну специфічних символів або слів
Форматування даних для виводу
Видалення або заміна чутливих даних перед виводом або збереженням

"""
text = "Hello world"
new_text = text.replace("world", "Python")
print(new_text) 


text = "one fish, two fish, red fish, blue fish"
new_text = text.replace("fish", "bird", 2)
print(new_text)  

xtext = "Hello, world!"
new_text = text.replace(" world", "")
print(new_text)


print('TestHook'.removeprefix('Test')) # Hook
print('TestHook'.removeprefix('Hook')) # TestHook

print('TestHook'.removesuffix('Test')) # TestHook
print('TestHook'.removesuffix('Hook')) # Test


url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
_, query = url_search.split('?')
print(query)
# операція url_search.split('?') розділяє URL 
# на дві частини: до знаку ? та після. 
# Оскільки нас цікавить лише частина після ?,
#  ми використовуємо символ _ для ігнорування частини URL до ?. 
# Та отримуємо змінну query яка рядок, що містить необхідні нам параметри запиту.

obj_query = {}
for el in query.split('&'):
    key, value = el.split('=')
    obj_query.update({key: value.replace('+', ' ')})
print(obj_query)




number = "12345"
print(number.isdigit())  # Виведе: True

text = "Number123"
print(text.isdigit())  # Виведе: False

#user_input = input("Введіть число: ")
user_input = '9'
if user_input.isdigit():
    print("Це дійсно число!")
else:
    print("Це не число!")


for char in "Hello 123":
    if char.isdigit():
        print(f"'{char}' - це цифра")
    else:
        print(f"'{char}' - не цифра")


# translate
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
print(trantab)
7

str = "This is string example"
print(str.translate(trantab))


intab = "aeiou"
trantab = str.maketrans('', '', intab)

print(trantab)
str = "This is string example"
print(str.translate(trantab))


"""
Програма повинна обробляти як великі, так і малі літери шістнадцяткових чисел і
 перетворювати кожен символ на його чотирибітове двійкове представлення.


"""
symbols = "0123456789ABCDEF"
code = [
        '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
        '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
        ]

MAP = {}

for s, c in zip(symbols, code):
    MAP[ord(s)] = c
    MAP[ord(s.lower())] = c

result = "34 DF 56 AC".translate(MAP)
print(result)



"""
Метод translate() є потужним інструментом, який пропонує більш
 гнучкі можливості порівняно з методом replace(), особливо коли 
 вам потрібно зробити багато різних замін у одному рядку.
"""

morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
              'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
              'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.'}

# Перетворення ключів словника на Unicode коди
table_morze_dict = {}
for k, v in morze_dict.items():
    table_morze_dict[ord(k)] = v

string = "Hello world"

result = ""

for ch in string:
    result = result + ch.upper().translate(table_morze_dict)

print(result)


for i in range(8):
    s = f"int: {i:d};  hex: {i:#x};  oct: {i:#o};  bin: {i:#b}"
    print(s)

"""
Вирівнювання визначає, як вміст буде вирівняний всередині вказаної ширини поля. Можливі варіанти вирівнювання:

<: Вирівнювання вмісту по лівому краю.
>: Вирівнювання вмісту по правому краю.
^: Вирівнювання вмісту по центру.
=: Використовується для вирівнювання чисел, при цьому знак (якщо він є) відображається зліва, а число - по правому краю поля.
"""
width = 5
for num in range(12):
    print(f'{num:^10} {num**2:^10} {num**3:^10}')


name = "Alice"
formatted = f"{name:>10}"
print(formatted)  # Виведе: '     Alice' (вирівнювання праворуч)


# f"{value:<ширина>.<точність>%}"

completion = 0.756
formatted = f"{completion:.1%}"
print(formatted)  # Виведе: '75.6%'

