def format_string(string: str, length: int):
    
    if len(string) >= length:
       # print(string)
        return str
    else:
        num_spaces = (length - len(string)) // 2
        centered_str = " " * num_spaces + string
        #print(centered_str)
        return centered_str

test1 ="Для створення рядка з пробілів використовуйте"
print(format_string(test1, 100))


def first(size, *args):
    #for arg in args:
    return size + len(args)

print(first(10, "test", 2, True, 1.2, [1, 2]))


def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def number_of_groups(n, k):
    
    return (factorial(n)/(factorial(n-k) * factorial(k)))


#a = number_of_groups(10, 2)
print(number_of_groups(10, 2))

print('test')
