from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    """Контроллер для домашней страницы"""
    return render(request, "home.html")


def contacts(request):
    """Контроллер для страницы контактов"""
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение принято и будет рассмотрено в ближайшее время.")
    return render(request, "contacts.html")
