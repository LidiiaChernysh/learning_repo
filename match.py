# Оператор match, введений у Python починаючи з версії 3.10, 
# є схожим на оператори switch-case в інших мовах програмування. 
# Він дозволяє порівнювати значення з декількома шаблонами і
#  виконувати різні блоки коду в залежності від того, який шаблон відповідає значенню. 
# Оператор match - це свого роду розширена і більш гнучка версія 
# оператора if-elif-else. Він дозволяє порівнювати значення з рядом шаблонів і, 
# залежно від відповідності, виконувати певні дії.

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


