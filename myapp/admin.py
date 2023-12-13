from django.contrib import admin

# Register your models here.
from .models import Product, Holiday, Purchase


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_type', 'material', 'has_stones', 'description']


class HolidayAdmin(admin.ModelAdmin):
    list_display = ['name', 'type_holiday', 'date', 'day_week', 'week', 'mounth', 'description']
    list_filter = ['date', 'mounth']

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['product', 'purchase_date', 'holiday']


admin.site.register(Product, ProductAdmin)
admin.site.register(Holiday, HolidayAdmin)
admin.site.register(Purchase, PurchaseAdmin)
