from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from blog.forms import BlogArticleForm
from blog.models import BlogArticle


class BlogArticleListView(ListView):
    """Контроллер со списком статей для домашней страницы"""

    model = BlogArticle
    template_name = "blogs/articles_list.html"
    context_object_name = "articles"

    def get_queryset(self):
        """Метод для отображения только опубликованных статей"""
        return BlogArticle.objects.filter(is_publication=True)


class BlogArticleDetailView(LoginRequiredMixin, DetailView):
    """Контроллер для отображения подробного содержания статьи"""

    model = BlogArticle
    template_name = "blogs/article_detail.html"
    context_object_name = "article"

    def get_object(self, queryset=None):
        """Метод для подсчета количества просмотров статьи"""
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogArticleCreateView(LoginRequiredMixin, CreateView):
    """Контроллер для добавления новой записи в блог"""

    model = BlogArticle
    form_class = BlogArticleForm
    template_name = "blogs/article_form.html"
    success_url = reverse_lazy("blog:articles_list")

    def form_valid(self, form):
        """Метод для переопределения валидации для автоматического добавления автора статьи"""
        article = form.save()
        user = self.request.user
        article.author = user
        article.save()
        return super().form_valid(form)


class BlogArticleUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер для изменения существующей записи"""

    model = BlogArticle
    form_class = BlogArticleForm
    template_name = "blogs/article_form.html"
    success_url = reverse_lazy("blog:articles_list")

    def get_success_url(self):
        """Метод для изменения адреса перенаправления после редактирования записи"""
        return reverse("blog:article_detail", args=[self.kwargs.get("pk")])


class BlogArticleDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер для удаления статьи"""

    model = BlogArticle
    template_name = "blogs/article_confirm_delete.html"
    success_url = reverse_lazy("blog:articles_list")
