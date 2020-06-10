from django.contrib import admin

# Register your models here.
from rest_framework import authtoken

from snippets.models import Snippet

admin.register(authtoken)


class SnippetAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'code']


admin.site.register(Snippet, SnippetAdmin)
