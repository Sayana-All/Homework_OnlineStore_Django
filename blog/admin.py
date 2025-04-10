from django.contrib import admin

from blog.models import BlogArticle


@admin.register(BlogArticle)
class AdminBlogArticle(admin.ModelAdmin):
    """Класс статей для админки"""

    list_display = ("id", "title", "created_at", "is_publication", "views_counter")
    list_filter = (
        "title",
        "created_at",
        "views_counter",
    )
    search_fields = ("id", "title", "created_at", "views_counter")
