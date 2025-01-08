##############
"""
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

"""

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i >= 6")


num = int(input("Enter the integer (0 to 100): "))
sum = 0

while num != 0:
    sum = sum + num
    num = num -1

print(sum)


message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = "r"
result = 0
for symbol in message:
    if symbol == search:
        result = result + 1
    else:
        continue

print(result)

