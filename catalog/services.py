from django.core.cache import cache

from catalog.models import Category, Product
from config.settings import CACHE_ENABLED


class ProductService:
    @staticmethod
    def get_product_from_cache():
        """Получение списка продуктов из кеша или из бд, если кеш пуст"""

        if not CACHE_ENABLED:
            return Product.objects.all()

        products = cache.get("products_list")

        if products is not None:
            return products
        products = Product.objects.all()
        cache.set("products_list", products)
        return products

    @staticmethod
    def get_products_by_category(category_id):
        """Получение списка продуктов по заданной категории"""

        if not CACHE_ENABLED:
            category = Category.objects.get(pk=category_id)
            products_by_category = Product.objects.filter(category=category)
            return products_by_category

        key = f"products_by_category_{category_id}"
        products = cache.get(key)
        if products is not None:
            return products

        category = Category.objects.get(pk=category_id)
        products_by_category = Product.objects.filter(category=category)
        cache.set(key, products_by_category)
        return products_by_category
