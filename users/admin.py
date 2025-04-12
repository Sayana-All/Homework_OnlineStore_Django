from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Класс управления пользователями для админки"""

    list_display = ("id", "email", "phone", "is_active")
    search_fields = ("email", "phone")
