from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    """Модель для профиля пользователя"""
    username = None
    email = models.EmailField(unique=True, verbose_name="Email", help_text="Введите адрес вашей почты")
    phone = PhoneNumberField(verbose_name="Номер телефона", blank=True, null=True, help_text="Введите номер телефона")
    country = models.CharField(max_length=50, verbose_name="Страна", blank=True, null=True, help_text="Укажите страну проживания")
    avatar = models.ImageField(upload_to="users/avatars/", verbose_name="Аватар", blank=True, null=True, help_text="Загрузите ваш аватар(изображение)")

    token = models.CharField(max_length=100, verbose_name="Токен", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
