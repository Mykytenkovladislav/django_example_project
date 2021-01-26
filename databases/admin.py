from django.contrib import admin  # noqa: F401

from .models import Quotes, QuotesAuthor


@admin.register(QuotesAuthor)
class QuotesAuthorModelAdmin(admin.ModelAdmin):
    list_display = ['author']


@admin.register(Quotes)
class QuotesModelAdmin(admin.ModelAdmin):
    list_display = ['quote', 'author']
