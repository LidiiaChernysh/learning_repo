empty_set = set()
a = set('hello')
b = {1, 2, 3, 4, 5}
numbers = {1, 2, 3, 1, 2, 3}

###
lst = [1, 2, 3, 1, 2, 2, 3, 4, 1]
d_lst = set(lst)
lst=list(d_lst)

########
numbers = {1, 2, 3}
numbers.add(4)
print(numbers)  # {1, 2, 3, 4}

### видаляє елемент із множини, викликає виняток, якщо такого елемента немає
numbers = {1, 2, 3}
numbers.remove(3)
print(numbers)  # {1, 2}

### видаляє елемент із множини і не викликає виняток, якщо його немає
numbers = {1, 2, 3}
numbers.discard(2)
print(numbers)  # {1, 3}

### 
a = {1, 2, 3}
b = {3, 4, 5}
print(a.intersection(b))  # {3}
print(a & b)  # {3}

###
a = {1, 2, 3}
b = {3, 4, 5}
print(a.difference(b))  # {1, 2}
print(a - b)  # {1, 2}

###
a = {1, 2, 3}
b = {3, 4, 5}
print(a.symmetric_difference(b))  # {1, 2, 4, 5}
print(a ^ b)  # {1, 2, 4, 5}

###
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))  # {1, 2, 3, 4, 5}
print(a | b)  # {1, 2, 3, 4, 5}

###
my_frozenset = frozenset([1, 2, 3, 4, 5])

###
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])

union = a | b  # Об'єднання множин
intersection = a & b  # Перетин множин
difference = a - b  # Різниця множин
symmetric_difference = a ^ b  # Симетрична різниця

print(union)  # frozenset({1, 2, 3, 4, 5})
print(intersection)  # frozenset({3})
print(difference)  # frozenset({1, 2})
print(symmetric_difference)  # frozenset({1, 2, 4, 5})

