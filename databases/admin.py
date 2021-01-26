from django.contrib import admin  # noqa: F401

from .models import QuotesAuthor, Quotes


@admin.register(QuotesAuthor)
class QuotesAuthorModelAdmin(admin.ModelAdmin):
    list_display = ['author']


@admin.register(Quotes)
class QuotesModelAdmin(admin.ModelAdmin):
    list_display = ['quote', 'author']
