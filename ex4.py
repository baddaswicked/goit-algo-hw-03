from datetime import datetime

users = [
    {"name": "John Doe", "birthday": "1985.03.08"},
    {"name": "Jane Smith", "birthday": "1990.03.08"}
]

def find_next_weekday(d,weekday:int):
    days_ahead=weekday-d.weekday()

    if days_ahead<=0:
        days_ahead+=7

    return d+timedelta(days=days_ahead)

def prapered(users):
    prepare_users=[]

    for user in users:
        try:
            birthday=datetime.strptime(user["birthday"], "%Y.%m.%d").date()
            prepare_users.append({"name":user["name"],"birthday":birthday})

        except ValueError:
            print(f"Некоректна дата  народження користувача {user['name']}")

    return prepare_users

def get_upcoming_birthdays(users):
    days=7
    today=datetime.today().date()
    upcoming_birthdays=[]

    for user in prapered(users):
        birthday_this_year=user["birthday"].replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year=user["birthday"].replace(year=today.year+1)
        if 0<=(birthday_this_year-today).days<=days:
            if birthday_this_year.weekday()>=5:
                birthday_this_year=find_next_weekday(birthday_this_year)#понеділок

            congrats=birthday_this_year.strftime("%Y.%m.%d")
            upcoming_birthdays.append({
                "name":user["name"],
                'congratulation_date':congrats
            })
    return upcoming_birthdays
print(get_upcoming_birthdays(users))