import datetime

from django import forms
from django.forms import NumberInput

from .models import Product, Purchase, Holiday


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'product_type', 'material', 'has_stones', 'description']


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['product', 'purchase_date', 'holiday']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'purchase_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'holiday': forms.Select(attrs={'class': 'form-control'}),
        }



class HolidaysFormWidget(forms.ModelForm):
    type_holiday = forms.ChoiceField(choices=[('D', 'по дате'), ('W', 'по дню недели')],
                                     widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    date = forms.IntegerField(required=False, min_value=1, max_value=31, widget=NumberInput(attrs={'class': 'form-control'}))


    class Meta:
        model = Holiday
        fields = ['name', 'type_holiday', 'date', 'day_week', 'week', 'mounth', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название праздника'}),
            'day_week': forms.Select(attrs={'class': 'form-control'}),
            'week': forms.Select(attrs={'class': 'form-control'}),
            'mounth': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(HolidaysFormWidget, self).__init__(*args, **kwargs)
        self.fields['type_holiday'].label = "Тип праздника"
        self.fields['date'].label = "Дата"

# class HolidaysFormWidget(forms.Form):
#     name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control',
#                                                          'placeholder': 'Название праздника'}))
#     type_holiday = forms.ChoiceField(choices=[('D', 'по дате'), ('W', 'по дню недели')],
#                                      widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
#     date = forms.DateField(initial=datetime.date.today,
#                                 widget=forms.DateInput(attrs={'class': 'form-control', 'type':
#                                     'date'}))
#     day_week = forms.ChoiceField(choices=[
#         (None, None),
#         ('1', 'понедельник'),
#         ('2', 'вторник'),
#         ('3', 'среда'),
#         ('4', 'четверг'),
#         ('5', 'пятница'),
#         ('6', 'суббота'),
#         ('7', 'воскресенье'),
#     ])
#     week = forms.ChoiceField(choices=[
#         (None, None),
#         ('1', 'первая неделя'),
#         ('2', 'второая неделя'),
#         ('3', 'третья неделя'),
#         ('4', 'четвертая неделя'),
#         ('5', 'пятая неделя'),
#     ])
#     mounth = forms.ChoiceField(choices=[
#         (None, None),
#         ('1', 'январь'),
#         ('2', 'февраль'),
#         ('3', 'март'),
#         ('4', 'апрель'),
#         ('5', 'май'),
#         ('6', 'июнь'),
#         ('7', 'июль'),
#         ('8', 'август'),
#         ('9', 'сентябррь'),
#         ('10', 'октябрь'),
#         ('11', 'ноябрь'),
#         ('12', 'декабрь'),
#     ])
#     description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':
#                                                                'form-control'}))


# class ManyFieldsFormWidget(forms.Form):
#     name = forms.CharField(max_length=50,
#                            widget=forms.TextInput(attrs={'class': 'form-control',
#                                                          'placeholder': 'Введите имя пользователя'}))
#
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class':
#                                                                 'form-control', 'placeholder': 'user@mail.ru'}))
#     age = forms.IntegerField(min_value=18,
#                              widget=forms.NumberInput(attrs={'class': 'form-control'}))
#     height = forms.FloatField(widget=forms.NumberInput(attrs={'class':
#                                                                   'form-control'}))
#     is_active = forms.BooleanField(required=False,
#                                    widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
#     birthdate = forms.DateField(initial=datetime.date.today,
#                                 widget=forms.DateInput(attrs={'class': 'form-control', 'type':
#                                     'date'}))
#     gender = forms.ChoiceField(choices=[('M', 'Male'), ('F',
#                                                         'Female')],
#                                widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
#     message = forms.CharField(widget=forms.Textarea(attrs={'class':
#                                                                'form-control'}))
