from django.db import models


class BlogArticle(models.Model):
    """Модель блоговой записи"""
    title = models.CharField(max_length=100, verbose_name="Заголовок", help_text="Введите заголовок записи")
    content = models.TextField(verbose_name="Содержимое", help_text="Введите текст записи")
    preview = models.ImageField(
        upload_to="preview/", blank=True, null=True, verbose_name="Изображение", help_text="Загрузите изображение для превью"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_publication = models.BooleanField(default=True, verbose_name="Признак публикации")
    views_counter = models.PositiveIntegerField(verbose_name="Количество просмотров", help_text="Укажите количество просмотров", default=0)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"
        ordering = [
            "title", "created_at", "views_counter",
        ]