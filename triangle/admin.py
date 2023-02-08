from django.contrib import admin

from .models import Log


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('path', 'method', 'timestamp', 'data', 'query')
    list_filter = ('path', 'method')
