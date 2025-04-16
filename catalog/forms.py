from django.core.exceptions import ValidationError
from django.forms import BooleanField, ModelForm

from catalog.models import Category, Product
from config.settings import FORBIDDEN_WORDS


class StyleFormMixin:
    """Класс для стилизации форм"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ProductForm(ModelForm):
    """Класс формы для создания и редактирования модели продуктов"""

    class Meta:
        model = Product
        exclude = ["owner", "created_at", "updated_at"]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"

        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите наименование товара"}
        )
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание товара"}
        )
        self.fields["photo"].widget.attrs.update({"class": "form-control"})
        self.fields["category"].widget.attrs.update({"class": "form-select"})
        self.fields["price"].widget.attrs.update({"class": "form-control", "placeholder": "Введите цену"})

    def clean_price(self):
        """Метод для проверки цены на отрицательные значения"""
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Цена не должна иметь отрицательное значение!")
        return price

    def clean(self):
        """Метод для проверки имени и описания на запрещенные слова"""
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        for word in FORBIDDEN_WORDS:
            if word in name.lower():
                self.add_error(
                    "name", "Внимание! Не используйте запрещенные слова в наименовании продукта (см. Справка)"
                )

            elif word in description.lower():
                self.add_error(
                    "description", "Внимание! Не используйте запрещенные слова в описании продукта (см. Справка)"
                )


class ProductModerateForm(StyleFormMixin, ModelForm):
    """Класс формы редактирования модели продуктов для модераторов"""

    class Meta:
        model = Product
        fields = ["is_publication"]


class CategoryForm(StyleFormMixin, ModelForm):
    """Класс формы для создания и редактирования модели категорий"""

    class Meta:
        model = Category
        fields = "__all__"
