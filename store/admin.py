from django.contrib import admin
from django.utils.html import format_html
from tinymce.widgets import TinyMCE
from django.db import models
from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from django.urls import reverse
from django.contrib import admin

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'display_image')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    readonly_fields = ('image_preview',)

    def display_image(self, obj):
        if obj.image:
            image_url = obj.image.url
            return format_html('<a href="{}"><img src="{}" width="50" height="50" /></a>', image_url, image_url)
        return None

    def image_preview(self, obj):
        return obj.image.url if obj.image else ''

    display_image.short_description = 'Image'
    image_preview.short_description = 'Image Preview'

    # Customize the display of the image in the admin list view
    display_image.short_description = 'Image'
    display_image.allow_tags = True

    # Customize the display of the image preview in the readonly view
    image_preview.short_description = 'Image Preview'

    # Add TinyMCE for the description field
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }



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
    list_display = ('product', 'customer', 'quantity', 'price', 'address', 'phone', 'date', 'status', 'display_image', 'total')
    list_filter = ('status',)
    # list_editable = ('status',)
    search_fields = ('customer__first_name', 'customer__last_name', 'product__name')
    readonly_fields = ('date', 'total')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('product', 'customer')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.placeOrder()
        super().save_model(request, obj, form, change)

    def display_image(self, obj):
        if obj.product.image:
            image_url = obj.product.image.url
            return format_html('<a href="{}"><img src="{}" width="50" height="50" /></a>', image_url, image_url)
        return None

    display_image.short_description = 'Product Image'

    def total(self, obj):
        return obj.product.price * obj.quantity
    total.short_description = 'Total'
