from django import template

register = template.Library()


@register.filter()
def media_filter(path):
    """Функция для фильтра медиа-ресурса моделей"""
    if path:
        return f"/media/{path}"
    else:
        return "/media/photos/no_image.jpg"
