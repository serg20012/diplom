from django.core.management.base import BaseCommand
from myapp.models import Product


class Command(BaseCommand):
    help = "read product."

    def handle(self, *args, **kwargs):
        one_product = Product.objects.all()
        self.stdout.write(f'{one_product}')
