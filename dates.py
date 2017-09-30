from datetime import datetime, timedelta
import calendar

dt_now = datetime.now()
print('Сегодня '+ str(dt_now))

delta = timedelta(days=1)

yesterday = dt_now-delta

print('Вчера '+str(yesterday))

my_month = calendar.monthrange(2017,8)

delta_month = timedelta(days = int(my_month[1]))

month_ago = dt_now - delta_month

print('Месяц назад '+str(month_ago))

