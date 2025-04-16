from catalog.models import Category
from config.settings import FORBIDDEN_WORDS


def categories_processor(request):
    return {
        "categories": Category.objects.all(),
    }


def forbidden_words_processor(request):
    return {
        "forbidden_words": FORBIDDEN_WORDS,
    }
