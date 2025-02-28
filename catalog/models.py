from django.db import models
from django.db.models import DateField


class Category(models.Model):
    """Класс для добавлений категорий продуктов"""

    name = models.CharField(max_length=50, verbose_name="Наименование", help_text="Введите название категории")
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание", help_text="Введите описание категории"
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = [
            "name",
        ]


class Product(models.Model):
    """Класс для добавления продукта"""

    name = models.CharField(max_length=100, verbose_name="Наименование", help_text="Введите наименование товара")
    description = models.TextField(verbose_name="Описание", help_text="Введите описание товара")
    photo = models.ImageField(
        upload_to="photos/", blank=True, null=True, verbose_name="Фотография", help_text="Загрузите фото товара"
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    price = models.IntegerField(verbose_name="Цена", help_text="Введите цену за покупку")
    created_at = DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")

    def __str__(self):
        return f"{self.name} по цене: {self.price}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name", "price", "category"]
