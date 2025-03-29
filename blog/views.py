from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from blog.models import BlogArticle


class BlogArticleListView(ListView):
    """Контроллер со списком статей для домашней страницы"""
    model = BlogArticle
    template_name = "blogs/articles_list.html"
    context_object_name = "articles"


class BlogArticleDetailView(DetailView):
    """Контроллер для отображения подробного содержания статьи"""
    model = BlogArticle
    template_name = "blogs/article_detail.html"
    context_object_name = "article"


class BlogArticleCreateView(CreateView):
    """Контроллер для добавления новой записи в блог"""
    model = BlogArticle
    fields = ["title", "content", "preview", "is_publication"]
    template_name = "blogs/article_form.html"
    success_url = reverse_lazy("blog:articles_list")


class BlogArticleUpdateView(UpdateView):
    """Контроллер для изменения существующей записи"""
    model = BlogArticle
    fields = ["title", "content", "preview", "is_publication"]
    template_name = "blogs/article_form.html"
    success_url = reverse_lazy("blog:articles_list")


class BlogArticleDeleteView(DeleteView):
    """Контроллер для удаления статьи"""
    model = BlogArticle
    template_name = "blogs/article_confirm_delete.html"
    success_url = reverse_lazy("blog:articles_list")
