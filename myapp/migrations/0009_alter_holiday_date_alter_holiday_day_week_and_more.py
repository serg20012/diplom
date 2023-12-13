# Generated by Django 5.0 on 2023-12-12 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_holiday_type_holiday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holiday',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='holiday',
            name='day_week',
            field=models.CharField(blank=True, choices=[('1', 'понедельник'), ('2', 'вторник'), ('3', 'среда'), ('4', 'четверг'), ('5', 'пятница'), ('6', 'суббота'), ('7', 'воскресенье')], max_length=1, null=True, verbose_name='День недели'),
        ),
        migrations.AlterField(
            model_name='holiday',
            name='description',
            field=models.TextField(verbose_name='Доп.инф-ция'),
        ),
        migrations.AlterField(
            model_name='holiday',
            name='mounth',
            field=models.CharField(blank=True, choices=[('1', 'январь'), ('2', 'февраль'), ('3', 'март'), ('4', 'апрель'), ('5', 'май'), ('6', 'июнь'), ('7', 'июль'), ('8', 'август'), ('9', 'сентябрь'), ('10', 'октябрь'), ('11', 'ноябрь'), ('12', 'декабрь')], max_length=2, null=True, verbose_name='Месяц'),
        ),
        migrations.AlterField(
            model_name='holiday',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='holiday',
            name='type_holiday',
            field=models.CharField(choices=[('D', 'по дате'), ('W', 'по дню недели')], max_length=1, verbose_name='по дате/по дню недели'),
        ),
        migrations.AlterField(
            model_name='holiday',
            name='week',
            field=models.CharField(blank=True, choices=[('1', 'первая неделя'), ('2', 'вторая неделя'), ('3', 'третья неделя'), ('4', 'четвертая неделя'), ('5', 'пятая неделя')], max_length=1, null=True, verbose_name='Неделя'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='has_stones',
            field=models.BooleanField(default=False, verbose_name='Камни'),
        ),
        migrations.AlterField(
            model_name='product',
            name='material',
            field=models.CharField(max_length=255, verbose_name='Основной материал'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(max_length=255, verbose_name='Тип изделия'),
        ),
    ]
