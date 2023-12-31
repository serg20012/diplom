# Generated by Django 5.0 on 2023-12-09 12:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holidays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='stone',
        ),
        migrations.RemoveField(
            model_name='product',
            name='type_product',
        ),
        migrations.AddField(
            model_name='product',
            name='has_stones',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='material',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occasion', models.CharField(max_length=255)),
                ('purchase_date', models.DateField()),
                ('holiday', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.holidays')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
            ],
        ),
    ]
