# Generated by Django 5.0 on 2023-12-12 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_holiday_date_alter_holiday_day_week_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holiday',
            name='day_week',
            field=models.CharField(blank=True, choices=[(None, None), ('1', 'понедельник'), ('2', 'вторник'), ('3', 'среда'), ('4', 'четверг'), ('5', 'пятница'), ('6', 'суббота'), ('7', 'воскресенье')], max_length=1, null=True, verbose_name='День недели'),
        ),
        migrations.AlterField(
            model_name='holiday',
            name='mounth',
            field=models.CharField(blank=True, choices=[(None, None), ('1', 'январь'), ('2', 'февраль'), ('3', 'март'), ('4', 'апрель'), ('5', 'май'), ('6', 'июнь'), ('7', 'июль'), ('8', 'август'), ('9', 'сентябрь'), ('10', 'октябрь'), ('11', 'ноябрь'), ('12', 'декабрь')], max_length=2, null=True, verbose_name='Месяц'),
        ),
        migrations.AlterField(
            model_name='holiday',
            name='week',
            field=models.CharField(blank=True, choices=[(None, None), ('1', 'первая неделя'), ('2', 'вторая неделя'), ('3', 'третья неделя'), ('4', 'четвертая неделя'), ('5', 'пятая неделя')], max_length=1, null=True, verbose_name='Неделя'),
        ),
    ]
