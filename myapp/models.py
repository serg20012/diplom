import datetime

from django.db import models


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    product_type = models.CharField(max_length=255, verbose_name="Тип изделия")  # кольцо, брошь и т.д.
    material = models.CharField(max_length=255, verbose_name="Основной материал")  # из чего сделано
    has_stones = models.BooleanField(default=False, verbose_name="Камни")  # наличие камней в украшении
    description = models.TextField(null=True, blank=True, verbose_name=u"Описание")
    rating = models.DecimalField(default=0.0, max_digits=3,
                                 decimal_places=2)
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class Holiday(models.Model):
    name = models.CharField(max_length=30, null=True, blank=False, verbose_name="Повод")
    type_holiday = models.CharField(max_length=2, choices=[('D', 'по дате'), ('W',
                                                'по дню недели')], verbose_name="Тип праздника")
    date = models.DateField(null=True, blank=True, verbose_name="Дата")
    day_week = models.CharField(max_length=1, choices=[
        (None, '-'),
        ('1', 'понедельник'),
        ('2', 'вторник'),
        ('3', 'среда'),
        ('4', 'четверг'),
        ('5', 'пятница'),
        ('6', 'суббота'),
        ('7', 'воскресенье'),
    ], null=True, blank=True, verbose_name="День недели")
    week = models.CharField(max_length=1, choices=[
        (None, '-'),
        ('1', 'первая неделя'),
        ('2', 'вторая неделя'),
        ('3', 'третья неделя'),
        ('4', 'четвертая неделя'),
        ('5', 'пятая неделя'),
    ], null=True, blank=True, verbose_name="Неделя")
    mounth = models.CharField(max_length=2, choices=[
        (None, '-'),
        ('1', 'январь'),
        ('2', 'февраль'),
        ('3', 'март'),
        ('4', 'апрель'),
        ('5', 'май'),
        ('6', 'июнь'),
        ('7', 'июль'),
        ('8', 'август'),
        ('9', 'сентябрь'),
        ('10', 'октябрь'),
        ('11', 'ноябрь'),
        ('12', 'декабрь'),
    ], null=True, blank=True, verbose_name="Месяц")
    description = models.TextField(null=True, blank=True, verbose_name="Доп.инф-ция")

    class Meta:
        verbose_name = "Праздник"
        verbose_name_plural = "Праздники"

    def __str__(self):
        return self.name

class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Название")  # Ссылка на украшение, которое было куплено
    purchase_date = models.DateField(default=datetime.date.today, verbose_name="Дата покупки")  # Дата покупки
    holiday = models.ForeignKey(Holiday, on_delete=models.SET_NULL, null=True,
                                blank=True, verbose_name="Повод")  # Ссылка на праздник (если есть)

    class Meta:
        verbose_name = "Покупку"
        verbose_name_plural = "Покупки"

    def __str__(self):
        return f'{self.product.name} - {self.holiday}'


