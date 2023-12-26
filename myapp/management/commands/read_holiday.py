from django.core.management.base import BaseCommand
from myapp.models import Product, Holiday


class Command(BaseCommand):
    help = "read holiday"

    # def add_arguments(self, parser):
    #     parser.add_argument('id', type=int, help='User ID')
    def my_view(request):
        today = date.today()
        return render(request, 'my_template.html', {'today': today})

    def handle(self, *args, **kwargs):
        data = dakwargs.pop('data')
        pk = kwargs['id']
        one_product = Holiday.objects.get(id=pk)
        print(f'{one_product.date}')
        self.stdout.write(f'{one_product.date}')
