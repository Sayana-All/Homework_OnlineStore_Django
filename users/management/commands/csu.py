from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = "Команда для создания суперпользователя"

    def handle(self, *args, **kwargs):
        user = User.objects.create(email="admin@example.com")
        user.set_password("qwerty25")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
