from datetime import datetime
date="2024-01.09"
def get_days_from_today(date):
    try:
        d=datetime.strptime(date, "%Y-%m-%d")
        today=datetime.now()
        t=today.date()-d.date()
        return t.days
    except ValueError:
        return "Not corect value of data"

print(get_days_from_today(date))
