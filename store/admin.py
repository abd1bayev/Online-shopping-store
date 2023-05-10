from django.contrib import admin
from django.utils.html import format_html

from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order


from django.contrib import admin
from .models import Products

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'display_image')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    readonly_fields = ('image_preview',)

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return None

    def image_preview(self, obj):
        return obj.image.url if obj.image else ''

    display_image.short_description = 'Image'
    image_preview.short_description = 'Image Preview'



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)



@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email')
    search_fields = ('first_name', 'last_name', 'email')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'customer', 'quantity', 'price', 'address', 'phone', 'date', 'status')
    list_filter = ('status',)
    search_fields = ('customer__first_name', 'customer__last_name', 'product__name')
    readonly_fields = ('date',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('product', 'customer')
