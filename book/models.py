from django.db import models
from django.urls import reverse

class Chapter(models.Model):
    title = models.CharField(max_length=255, verbose_name="Назва глави")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField(blank=True, verbose_name="Опис")
    text = models.TextField(verbose_name="Текст глави")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Час створення")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Час зміни")
    is_published = models.BooleanField(default=True, verbose_name="Опубліковано")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('chapter', kwargs={'chapter_slug': self.slug})

    class Meta:
        verbose_name = 'Глава'
        verbose_name_plural = 'Глави'
        ordering = ['id', 'title', 'time_create']
