from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    ContactsTemplateView

app_name = CatalogConfig.name

urlpatterns = [
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path("", ProductListView.as_view(), name="product_list"),
    path("product_detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product_detail/<int:pk>/edit", ProductUpdateView.as_view(), name="product_edit"),
    path("product_detail/<int:pk>/delete", ProductDeleteView.as_view(), name="product_delete"),
    path("create/", ProductCreateView.as_view(), name="add_product"),
]
