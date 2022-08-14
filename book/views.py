from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from jinja2 import Template
# from .forms import *
from .models import *
from .utils import *
import datetime


class Home(DataMixin, ListView):  # homepage
    model = Chapter
    template_name = 'book/index.html'
    context_object_name = 'chapters'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Грокаємо алгоритми")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Chapter.objects.filter(is_published=True)


def pageNotFound(request, exception):  # pageNotFound
    return HttpResponseNotFound('<h1>Сторінку не знайдено</h1>')


class ShowChapter(DataMixin, DetailView):  # singleproduct
    model = Chapter
    template_name = 'book/chapter.html'
    slug_url_kwarg = 'chapter_slug'
    context_object_name = 'chapter'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['chapter'])
        return dict(list(context.items()) + list(c_def.items()))


def about_book(request):
    chapters = Chapter.objects.filter(is_published=True)
    context = {
        'chapters': chapters,
        'title': 'Про книгу'
    }
    return render(request, 'book/about_book.html', context)


def about_author(request):
    chapters = Chapter.objects.filter(is_published=True)
    context = {
        'chapters': chapters,
        'title': 'Про автора'
    }
    return render(request, 'book/about_author.html', context)


def chapters(request):
    chapters = Chapter.objects.filter(is_published=True)
    context = {
        'chapters': chapters,
        'title': 'Зміст книги'
    }
    return render(request, 'book/chapters.html', context)


def answers(request):
    chapters = Chapter.objects.filter(is_published=True)
    context = {
        'chapters': chapters,
        'title': 'Відповіді на вправи'
    }
    return render(request, 'book/answers.html', context)


def about_translation(request):
    chapters = Chapter.objects.filter(is_published=True)
    context = {
        'chapters': chapters,
        'title': 'Про переклад',
    }
    return render(request, 'book/about_translation.html', context)
