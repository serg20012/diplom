# Generated by Django 5.0 on 2023-12-10 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_purchase_holiday_delete_holidays'),
    ]

    operations = [
        migrations.RenameField(
            model_name='holiday',
            old_name='month',
            new_name='mounth',
        ),
        migrations.AlterField(
            model_name='holiday',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]