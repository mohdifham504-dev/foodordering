# product/admin.py
from django.contrib import admin
from .models import Product, Productmetainformation, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("Product_name", "product_price", "product_demo_price", "product_slug")
    prepopulated_fields = {"product_slug": ("Product_name",)}
    inlines = [ProductImageInline]

@admin.register(Productmetainformation)
class ProductMetaAdmin(admin.ModelAdmin):
    list_display = ("product", "product_quantity", "product_measuring", "is_restricted", "restricted_quantity")


# Register your models here.
