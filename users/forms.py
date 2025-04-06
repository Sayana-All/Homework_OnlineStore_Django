from django.contrib.auth.forms import UserCreationForm
from django.forms import BooleanField

from users.models import User


class StyleFormMixin:
    """Класс для стилизации форм"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    """Класс формы для регистрации нового пользователя"""

    class Meta:
        model = User
        fields = ("email", "password1", "password2")
