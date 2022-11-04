from django.contrib import admin
from .models import Category,Product


@admin.register(Category)
class CategeryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProducAdmin(admin.ModelAdmin):
    list_display = ['title','author','slug','price',
                    'in_stock','created', 'updated']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}