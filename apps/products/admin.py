from django.contrib import admin
from .models import Product, ProductHistory

# Register your models here.
admin.site.register(ProductHistory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display= ('name', 'base_price_currency', 'base_price')