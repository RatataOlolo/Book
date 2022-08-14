from django.urls import path, re_path

from .views import *
from . import views

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('chapter/<slug:chapter_slug>/', ShowChapter.as_view(), name='chapter'),
    path('about_book/', about_book, name='about_book'),
    path('about_author/', about_author, name='about_author'),
    path('chapters/', chapters, name='chapters'),
    path('answers/', answers, name='answers'),
    path('about_translation/', about_translation, name='about_translation'),
]
