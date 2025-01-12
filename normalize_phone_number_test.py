import re 


def normalize_phone(phone_number:str) -> str:
    """
    Function normalizes phone numbers to the standard format, 
    leaving only the digits and the '+' symbol at the beginning.
    The function removes all characters except digits and the '+' symbol.
    If the international code is missing, the function adds the code '+38',
    when the number starts with '380' - only '+' is added, and when 
    the number starts without a code - '+38' is added.

    Parameters:
        phone_number (str): a string with a phone number in various formats.
    
    Returns:
        str: returns the normalized phone number as a string.
    """
    #if len < 10:
       # return f'incorrect number'
    pass

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "0633801642",
    "80633801642",
    "+0630101010",
    "+80630101010"
]

#sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
#print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

# delete all symbols exept "+"
pattern_delete_all_symb = r"[^+\d]"
replacement = ""

# separate contry code and main part of the number
pattern = r"([+]|\d+|[+]\d+)0(\d+)"

for phone in raw_numbers:
    phone_without_symbols = re.sub(pattern_delete_all_symb, replacement, phone)

    first_2_symb = phone_without_symbols[0:2]

    if phone_without_symbols[0] == "0":
        formatted_phone = "+38" + phone_without_symbols
        print(formatted_phone)
    elif first_2_symb == "38":
        formatted_phone = "+" + phone_without_symbols
        print(formatted_phone)
    elif first_2_symb == "80":
        formatted_phone = "+3" + phone_without_symbols
        print(formatted_phone)
    elif first_2_symb == "+0":
        formatted_phone = phone_without_symbols.replace("+", "+38")
        print(formatted_phone)
    elif first_2_symb == "+8":
        formatted_phone = phone_without_symbols.replace("+8", "+38")
        print(formatted_phone)
    else:
        print(phone_without_symbols)
    
 


# pattern = r"([+]|\d+|[+]\d+)0(\d+)"
# match = re.search(pattern, "0630101010")

# if match:
#     contry_code = match.group(1)
#     main_phone = match.group(2)
# print(contry_code, main_phone)

# pattern = r"(\d{+})(\d{10})"
# replacement = r"(\1\2"
# formatted_phone = re.sub(pattern, replacement, "+0630101010")

# print(formatted_phone)