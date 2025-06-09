from django.contrib import admin
from .models import Product
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','slug', 'price', 'stock','category','is_available','modified_date']
    prepopulated_fields = {'slug' : ('product_name',)}