# Generated by Django 5.0 on 2023-12-07 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type_product', models.CharField(max_length=100)),
                ('material', models.CharField(max_length=100)),
                ('stone', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='products/')),
            ],
        ),
    ]
