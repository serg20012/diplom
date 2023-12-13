# Generated by Django 5.0 on 2023-12-12 13:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_holiday_day_week_alter_holiday_mounth_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='occasion',
        ),
        migrations.AlterField(
            model_name='holiday',
            name='type_holiday',
            field=models.CharField(choices=[('D', 'по дате'), ('W', 'по дню недели')], max_length=2, verbose_name='Тип праздника'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='holiday',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.holiday', verbose_name='Повод'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product', verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='purchase_date',
            field=models.DateField(verbose_name='Дата покупки'),
        ),
    ]