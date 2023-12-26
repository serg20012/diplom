from datetime import date, timedelta, datetime

from django.core.management import BaseCommand

from myapp.models import Holiday, Purchase


# функция получения даты от дня недели и порядковой недели месяца
def get_date_for_weekday(weekday, week_number, month, year=None):
    if year is None:
        year = date.today().year
    print(year)
    # Находим дату с первым днем недели месяца
    for i in range(1, 8):
        print(i, "circle")
        target_date = date(year, month, i)
        if target_date.weekday() == weekday:
            print(f' нашли - {target_date.weekday()}  - {target_date}')
            break
    # Добавляем нужное количество недель к найденной дате
    target_date = target_date + timedelta(weeks=week_number - 1)
    return target_date  # формат даты


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

        # print(res)
    return res

i = get_holiday(30)




for item in i:
    for holiday in item:
        print(f"на праздник: {holiday.name}")
        purchase = Purchase.objects.filter(holiday__id=holiday.id)
        if not purchase.exists():
            print("покупок не было")
        else:
            for i in purchase:
                print(f"было куплено: {i}")


#
#
def get_purchase(hol_id):
    hol = get_holiday(30)
    purchase = Purchase.objects.filter(holiday__id=hol_id)
    print(purchase)
    return purchase

# print(get_purchase(3))


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print(Holiday.objects.get(month=2))