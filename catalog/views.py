from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from unicodedata import category

from catalog.forms import ProductForm, ProductModerateForm
from catalog.models import Product, Category
from catalog.services import ProductService
from config.settings import forbidden_words


class ProductListView(ListView):
    """Контроллер со списком продуктов для домашней страницы"""

    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        return ProductService.get_product_from_cache()

    def get_context_data(self, **kwargs):
        """Переопределяем метод для добавления списка запрещенных слов в форму"""
        context = super().get_context_data(**kwargs)
        context["forbidden_words"] = forbidden_words
        return context


@method_decorator(cache_page(300), name="dispatch")
class ProductDetailView(LoginRequiredMixin, DetailView):
    """Контроллер для отображения детальной информации о продукте"""

    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Контроллер для добавления нового продукта"""

    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def get_context_data(self, **kwargs):
        """Переопределяем метод для добавления списка запрещенных слов в форму"""
        context = super().get_context_data(**kwargs)
        context["forbidden_words"] = forbidden_words
        context["categories"] = Category.objects.all()
        return context

    def form_valid(self, form):
        """Метод для переопределения валидации для автоматического добавления владельца товара"""
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер для редактирования существующего продукта"""

    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def get_success_url(self):
        """Метод для изменения адреса перенаправления после редактирования записи"""
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])

    def get_form_class(self):
        """Добавляем форму для модератора при наличии прав"""
        user = self.request.user
        if user == self.object.owner or user.has_perm("catalog.change_product"):
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModerateForm
        raise PermissionDenied

    def get_context_data(self, **kwargs):
        """Переопределяем метод для добавления списка запрещенных слов в форму"""
        context = super().get_context_data(**kwargs)
        context["forbidden_words"] = forbidden_words
        return context


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Контроллер для удаления продукта"""

    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")

    def test_func(self):
        """Добавляем форму для модератора при наличии прав"""

        user = self.request.user
        return user == self.get_object().owner or user.has_perm("catalog.delete_product")


class ProductsByCategoryListView(LoginRequiredMixin, ListView):
    """Контроллер для категории со списком входящих в нее продуктов"""

    model = Category
    template_name = "catalog/products_by_category.html"
    context_object_name = "products"

    def get_queryset(self):
        category_id = self.kwargs.get("pk")
        return ProductService.get_products_by_category(category_id=category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.get(pk=self.kwargs.get("pk"))
        context["categories"] = Category.objects.all()
        return context


class ContactsTemplateView(LoginRequiredMixin, TemplateView):
    """Контроллер для страницы контактов"""

    template_name = "catalog/contacts.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение принято и будет рассмотрено в ближайшее время.")
