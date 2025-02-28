from django.contrib import admin
from catalog.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Класс категорий для админки"""
    list_display = ("id", "name")
    search_fields = ("name", "description")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Класс категорий для админки"""
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name", "description", "category__name")
