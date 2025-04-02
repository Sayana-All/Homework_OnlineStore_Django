from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from catalog.models import Product


class ProductListView(ListView):
    """Контроллер со списком продуктов для домашней страницы"""
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    """Контроллер для отображения детальной информации о продукте"""
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ProductCreateView(CreateView):
    """Контроллер для добавления нового продукта"""
    model = Product
    fields = ["name", "description", "photo", "category", "price"]
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(UpdateView):
    """Контроллер для редактирования существующего продукта"""
    model = Product
    fields = ["name", "description", "photo", "category", "price"]
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")


class ProductDeleteView(DeleteView):
    """Контроллер для удаления продукта"""
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")


class ContactsTemplateView(TemplateView):
    """Контроллер для страницы контактов"""
    template_name = "catalog/contacts.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение принято и будет рассмотрено в ближайшее время.")