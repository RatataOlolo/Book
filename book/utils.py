from django.db.models import Count
from .models import *

menu = [{'title': 'Головна', 'url_name': 'home'},
        {'title': 'Про книгу', 'url_name': 'about_book'},
        {'title': 'Про автора', 'url_name': 'about_author'},
        {'title': 'Глави', 'url_name': 'chapters'},
        {'title': 'Відповіді на вправи', 'url_name': 'answers'},
        {'title': 'Про переклад', 'url_name': 'about_translation'},
        ]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        chapters = Chapter.objects.filter(is_published=True)

        context['menu'] = menu
        context['chapters'] = chapters

        return context
