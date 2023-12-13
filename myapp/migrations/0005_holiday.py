# Generated by Django 5.0 on 2023-12-10 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_holidays_remove_product_stone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('date', models.DateField(blank=True, null=True)),
                ('day_week', models.CharField(blank=True, choices=[('1', 'понедельник'), ('2', 'вторник'), ('3', 'среда'), ('4', 'четверг'), ('5', 'пятница'), ('6', 'суббота'), ('7', 'воскресенье')], max_length=1, null=True)),
                ('week', models.CharField(blank=True, choices=[('1', 'первая неделя'), ('2', 'вторая неделя'), ('3', 'третья неделя'), ('4', 'четвертая неделя'), ('5', 'пятая неделя')], max_length=1, null=True)),
                ('month', models.CharField(blank=True, choices=[('1', 'январь'), ('2', 'февраль'), ('3', 'март'), ('4', 'апрель'), ('5', 'май'), ('6', 'июнь'), ('7', 'июль'), ('8', 'август'), ('9', 'сентябрь'), ('10', 'октябрь'), ('11', 'ноябрь'), ('12', 'декабрь')], max_length=2, null=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
