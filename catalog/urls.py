from django.urls import path

from catalog import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", views.home, name="home"),
    path("contacts/", views.contacts, name="contacts"),
    path("product_detail/<int:pk>/", views.product_detail, name="product_detail"),
]
