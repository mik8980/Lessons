# Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
from datetime import datetime, timedelta

dt_now = datetime.now()
delta = timedelta(days=1)
delta2 = timedelta(days=30)
print(dt_now - delta2)
print(dt_now - delta)
print(dt_now.now())


# Превратите строку "01/01/25 12:10:03.234567" в объект datetime
date = datetime.strptime('01/01/25 12:10:03.234567', '%d/%m/%y %H:%M:%S.%f')
print(date)