from datetime import datetime, timedelta
given_date = datetime(2020, 3, 22, 10, 0, 0)
new_date=given_date + timedelta(days=7,hours=12)
print(new_date.strftime("%Y-%m-%d %H:%M:%S"))
