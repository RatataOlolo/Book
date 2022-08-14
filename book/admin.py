from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from django.contrib.sessions.models import Session


class ChapterAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'time_update', 'description', 'is_published')  # fields that will be show in admin panel
    list_display_links = ('id', 'title')  # fields that will be links
    search_fields = ('title', 'description')  # fields that will be searched
    list_editable = ('is_published',)  # fields that will be editable in admin panel
    list_filter = ('is_published', 'time_create', 'time_update')  # for filter by this fields in admin panel
    prepopulated_fields = {'slug': ('title',)}  # for autofilling url-slug

admin.site.register(Chapter, ChapterAdmin)  # two classes for register class with fields

