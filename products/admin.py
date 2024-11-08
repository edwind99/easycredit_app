from django.contrib import admin

from .models import Product, ProductType

# Register your models here.

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_type', 'name', 'price', 'stock', 'description']
    search_fields = ['name']