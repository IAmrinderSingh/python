import calendar
from datetime import date
today=date.today()
year=today.year
months=today.month
print(calendar.month(year,months))