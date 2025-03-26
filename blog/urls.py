from django.urls import path

from blog.apps import BlogConfig
from blog.views import

app_name = BlogConfig.name

urlpatterns = [
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path("", ProductListView.as_view(), name="product_list"),
    path("product_detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product_detail/<int:pk>/edit", ProductUpdateView.as_view(), name="product_edit"),
    path("product_detail/<int:pk>/delete", ProductDeleteView.as_view(), name="product_delete"),
    path("create/", ProductCreateView.as_view(), name="add_product"),
]