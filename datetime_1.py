from datetime import datetime, timedelta  # type: ignore

now = datetime.now()
print(now.date())


# Встановлення дати спалення Москви Наполеоном (14 вересня 1812 року)
napoleon_burns_moscow = datetime(year=1812, month=9, day=14)

# Поточна дата
current_date = datetime.now()

# Розрахунок кількості днів
days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
#print(days_since)





next_day = now + timedelta(1)
#print(next_day.date()) # only date without time

some_date =  datetime(year=2024, month=12, day=25)
print("Yes" if now.date() <= some_date.date() < (now + timedelta(7)).date() else "No")


def string_to_date(date_string: str):
    parsed_date = datetime.strptime(date_string, "%Y.%m.%d")
    date_only = parsed_date.date()

    return date_only

users = [{"name": "Bill Gates", "birthday": "1955.3.25"}]

#print(string_to_date(datetime(users["birthday"])))


today1 = datetime(2024, 12, 28)
today = today1.date()
print(today + timedelta(7))
