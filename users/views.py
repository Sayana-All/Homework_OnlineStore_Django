from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from users.forms import UserRegisterForm
from users.models import User


class UserCreateView(CreateView):
    """Контроллер для регистрации пользователя"""

    model = User
    form_class = UserRegisterForm
    template_name = "users/registration_form.html"
    success_url = reverse_lazy("users:login")
