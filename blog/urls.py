from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogArticleListView, BlogArticleDetailView, BlogArticleUpdateView, BlogArticleCreateView, BlogArticleDeleteView


app_name = BlogConfig.name

urlpatterns = [
    path("", BlogArticleListView.as_view(), name="articles_list"),
    path("article_detail/<int:pk>/", BlogArticleDetailView.as_view(), name="article_detail"),
    path("article_detail/<int:pk>/edit", BlogArticleUpdateView.as_view(), name="article_edit"),
    path("article_detail/<int:pk>/delete", BlogArticleDeleteView.as_view(), name="article_delete"),
    path("create/", BlogArticleCreateView.as_view(), name="add_article"),
]