# Generated by Django 5.0 on 2023-12-12 13:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_remove_purchase_occasion_alter_holiday_type_holiday_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='purchase_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата покупки'),
        ),
    ]
