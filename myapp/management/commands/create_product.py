from django.core.management.base import BaseCommand
from myapp.models import Product


class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        one_product = Product(
            name='Кольцо обручальное',
            type_product='кольцо',
            material='золото',
            stone='нет',
            price='100',
            description='что еще',
        )
        one_product.save()
        self.stdout.write(f'{one_product}')
