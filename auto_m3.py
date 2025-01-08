from datetime import datetime, timedelta, date


users = [
    {"name": "Bill Gates", "birthday": "1955.12.25"},
    {"name": "Steve Jobs", "birthday": "1955.12.21"},
    {"name": "Jinny Lee", "birthday": "1956.12.28"},
    {"name": "John Doe", "birthday": "1985.01.01"},
    {"name": "Jane Smith", "birthday": "1990.01.04"}
]

def string_to_date(date_string):
    parsed_date = datetime.strptime(date_string, "%Y.%m.%d")
    date_only = parsed_date.date()

    return date_only



def date_to_string(date):
    return date.strftime("%Y.%m.%d")
 # type: ignore



def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    #print(prepared_list, type(prepared_list))
    return prepared_list

def find_next_weekday(start_date, weekday):
    day_of_week = start_date.weekday()
    days_ahead = int(weekday) - int(day_of_week)

    if days_ahead <= 0:
        days_ahead = days_ahead + 7
    else: 
        pass

    greeting_day = start_date + timedelta(days_ahead) 
    #print("Greeting day: ", greeting_day)
    weekday_of_greeting = int(greeting_day.weekday())
    if weekday_of_greeting == 5:
        greeting_day = greeting_day + timedelta(2)
    elif weekday_of_greeting == 6:
        greeting_day = greeting_day + timedelta(1)
    else:
        pass 

    return greeting_day



def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:
        return find_next_weekday(birthday, 0)
    return birthday


def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()
    # today1 = datetime(2024, 12, 29)
    # today = today1.date()
    next_year = today.year + 1

    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)

        """
        Додайте на цьому місці перевірку, чи не буде 
        припадати день народження вже наступного року.
        """
        

        if birthday_this_year < today:
            try:
                next_year_birthday = birthday_this_year.replace(year=next_year)
            except ValueError:  # Handle February 29 to non-leap year
                next_year_birthday = birthday_this_year + timedelta(days=365)

            if next_year_birthday <= (today + timedelta(7)):
                birthday_this_year = next_year_birthday
        
            

        if today <= birthday_this_year < (today + timedelta(7)):
            
            
            """
            Додайте перенесення дати привітання на наступний робочий день,
            якщо день народження припадає на вихідний. 
            """
            congratulation_date = adjust_for_weekend(birthday_this_year)
            congratulation_date_str = date_to_string(congratulation_date)
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})
        else:
            pass
        

    return upcoming_birthdays

#print(users)
now = datetime.now()

print(get_upcoming_birthdays(prepare_user_list(users), days=7))
