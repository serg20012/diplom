from datetime import timedelta, datetime, date

from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProductForm, PurchaseForm, HolidaysFormWidget, GetDeltaWidget

from .models import Product, Holiday, Purchase
from .my_func.get_holiday import get_holiday


# Create your views here.
def test(request):
    return HttpResponse("test")


def check_holiday(request):
    result = None
    if request.method == 'POST':
        form = GetDeltaWidget(request.POST)
        message = "Ошибка в данных"
        if form.is_valid():
            if 'date_delta' in form.cleaned_data:
                date_delta = form.cleaned_data['date_delta']
                result = get_holiday(date_delta)
                # Извлечение данных о покупках для каждого праздника
                for item in result:
                    for holiday in item:
                        holiday.purchase_data = Purchase.objects.filter(holiday__id=holiday.id).select_related(
                            'holiday')
                message = 'Ок'
            else:
                pass

    else:
        form = GetDeltaWidget()
        message = 'Введите период (кол-во дней)'
    return render(request, 'myapp/check_holiday.html',
                  {'form': form, 'message': message, 'result': result})


def index(request):
    return render(request, "myapp/index.html")


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        message = "Ошибка в данных"
        if form.is_valid():
            form.save()
            message = 'продукт сохранен'
    else:
        form = ProductForm()
        message = 'Заполните данные'
    return render(request, 'myapp/add_product.html',
                  {'form': form, 'message': message})


def add_purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        message = "Ошибка в данных"
        if form.is_valid():
            form.save()
            message = 'Покупка сохранена'
    else:
        form = PurchaseForm()
        message = 'Заполните данные'
    return render(request, 'myapp/add_purchase.html',
                  {'form': form, 'message': message})

def add_holiday(request):
    if request.method == 'POST':
        form = HolidaysFormWidget(request.POST)
        message = "Ошибка в данных"
        if form.is_valid():
            name = form.cleaned_data['name']
            date = form.cleaned_data['date']
            day_week = form.cleaned_data['day_week']
            week = form.cleaned_data['week']
            month = form.cleaned_data['month']
            description = form.cleaned_data['description']
            holiday = Holiday(name=name, date=date, day_week=day_week, week=week, month=month, description=description)
            holiday.save()
            message = 'Праздник сохранен'
    else:
        form = HolidaysFormWidget()
        message = 'Заполните данные'
    return render(request, 'myapp/add_holiday.html',
                  {'form': form, 'message': message})


def product_list(request):
    return render(request, "myapp/index.html")


