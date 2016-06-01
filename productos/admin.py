from django.contrib import admin
from .models import Product, Category, ProductImage

# Register your models here.
@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    pass

@admin.register(Category)
class AdminCategoty(admin.ModelAdmin):
    pass


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass