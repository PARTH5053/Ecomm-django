from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'slug', 'category_image']
    prepopulated_fields = {'slug' : ('category_name',)}
    