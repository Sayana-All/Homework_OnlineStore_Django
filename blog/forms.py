from django.forms import BooleanField, ModelForm

from blog.models import BlogArticle


class StyleFormMixin:
    """Класс для стилизации форм"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class BlogArticleForm(StyleFormMixin, ModelForm):
    """Класс формы для создания и редактирования модели продуктов"""

    class Meta:
        model = BlogArticle
        exclude = ["author", "created_at", "views_counter"]
