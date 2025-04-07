from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from catalog.forms import ProductForm
from catalog.models import Product
from config.settings import forbidden_words


class ProductListView(ListView):
    """Контроллер со списком продуктов для домашней страницы"""

    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "products"


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
        return context


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер для редактирования существующего продукта"""

    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def get_success_url(self):
        """Метод для изменения адреса перенаправления после редактирования записи"""
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])

    def get_context_data(self, **kwargs):
        """Переопределяем метод для добавления списка запрещенных слов в форму"""
        context = super().get_context_data(**kwargs)
        context["forbidden_words"] = forbidden_words
        return context

    # def get_context_data(self, **kwargs):
    #    """Метод для изменения и добавления новой категории товара"""
    #    context_data = super().get_context_data(**kwargs)
    #    ProductFormset = inlineformset_factory(Product, Category, CategoryForm, extra=1)
    #    if self.request.method == "POST":
    #        context_data["formset"] = ProductFormset(self.request.POST, instance=self.object)
    #    else:
    #        context_data["formset"] = ProductFormset(instance=self.object)
    #    return context_data


#
# def form_valid(self, form):
#    """Метод для переопределения валидации формы"""
#    context_data = self.get_context_data()
#    formset = context_data["formset"]
#    if form.is_valid() and formset.is_valid():
#        self.object = form.save()
#        formset.instance = self.object
#        formset.save()
#        return super().form_valid(form)
#    else:
#        return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер для удаления продукта"""

    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")


class ContactsTemplateView(LoginRequiredMixin, TemplateView):
    """Контроллер для страницы контактов"""

    template_name = "catalog/contacts.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение принято и будет рассмотрено в ближайшее время.")
