import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
import django
django.setup()
# -------------выше для успешного тестирования
from datetime import date, timedelta, datetime
from myapp.models import Holiday

# функция получения праздников в диапазоне
def get_holiday(date_delta, today=None): # параметр today для тестирования функции
    if today is None:
        today = date.today()
    end_date = today + timedelta(days=date_delta)
    res = []
    # print(f' начальный месяц - {today.month}  конечный месяц - {end_date.month}') #тест
    # print(f' начальное число - {today.day} конечное число - {end_date.day}') #тест
    # print(f' сегодня - {today}, {today.weekday()}') #тест

    # цикл перебора дат в диапозоне
    for td in range(date_delta + 1):
        curent_day = (today + timedelta(days=td)).day # -> int
        curent_month = (today + timedelta(days=td)).month # ->int
        current_year = (today + timedelta(days=td)).year # ->int
        # получение первого дня месяца для вычисления порядковой недели
        date1 = datetime(current_year, curent_month, 1)
        curent_week = (curent_day + date1.weekday() - 1) // 7 + 1

        curent_weekday = (datetime(current_year, curent_month, curent_day)).weekday() # ->int 0-6

        # print(f'месяц - {curent_month}, число - {curent_day},'
        #       f' неделя - {curent_week}, день недели - {curent_weekday}') #тест

        holidays = Holiday.objects.filter(month=curent_month, date=curent_day)
        if holidays.exists():
            res.append(holidays)
        holidays2 = Holiday.objects.filter(month=curent_month, type_holiday='W',
                                           week=curent_week, day_week=curent_weekday + 1)
        if holidays2.exists():
            res.append(holidays2)
    return res

if __name__ == '__main__':
    i = get_holiday(30)
    for item in i:
        print(item)
        for holiday in item:
            print(f"Holiday ID: {holiday.id}, Name: {holiday.name}")
