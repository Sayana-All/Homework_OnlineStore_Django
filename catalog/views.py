from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from catalog.models import Product, Category


def home(request):
    """Контроллер для домашней страницы"""
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "home.html", context)


def contacts(request):
    """Контроллер для страницы контактов"""
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение принято и будет рассмотрено в ближайшее время.")
    return render(request, "contacts.html")


def product_detail(request, pk):
    """Контроллер для домашней страницы"""
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "product_detail.html", context)


def add_product(request):
    """Контроллер для страницы контактов"""
    categories = Category.objects.all()
    context = {"categories": categories}

    if request.method == "POST":
        product = Product.objects.create(
            name=request.POST.get("name"),
            description=request.POST.get("description"),
            photo=request.POST.get("photo"),
            category=request.POST.get("category"),
            price=request.POST.get("price"),
        )
        product.save()
        return HttpResponse(f"Спасибо, товар {product.name} добавлен в каталог! Можете посмотреть его на странице")

    return render(request, "add_product.html", context)
