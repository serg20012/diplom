from django.shortcuts import render
from django.http import HttpResponse
from jinja2 import Template


from .forms import ProductForm, PurchaseForm, HolidaysFormWidget
from .models import Product, Holiday


# Create your views here.
def test(request):
    return HttpResponse("test")


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
            mounth = form.cleaned_data['mounth']
            description = form.cleaned_data['description']
            holiday = Holiday(name=name, date=date, day_week=day_week, week=week, mounth=mounth, description=description)
            holiday.save()
            message = 'Праздник сохранен'
    else:
        form = HolidaysFormWidget()
        message = 'Заполните данные'
    return render(request, 'myapp/add_holiday.html',
                  {'form': form, 'message': message})


def product_list(request):
    return render(request, "myapp/index.html")


# def many_fields_form(request):
#     if request.method == 'POST':
#         form = ManyFieldsFormWidget(request.POST)
#         if form.is_valid():
#             print('444')
#             # Делаем что-то с данными
#
#     else:
#         form = ManyFieldsFormWidget()
#     return render(request, 'myapp/add_product.html', {'form': form})
