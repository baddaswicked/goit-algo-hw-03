from datetime import datetime
date="2024-01.09"
def get_days_from_today(date):
    d=datetime.strptime(date, "%Y-%m-%d")
    today=datetime.now()
    return d
print(get_days_from_today(date))
