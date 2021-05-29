from django.contrib import admin
from django.contrib.admin import ModelAdmin

from todo.models import Todo


@admin.register(Todo)
class TodoAdmin(ModelAdmin):
    readonly_fields = ('slug',)
    fields = ('type', 'key', 'summary', 'assignee', 'reporter', 'priority', 'status')
    list_display = ('type', 'key', 'summary', 'assignee', 'reporter', 'priority', 'status', 'created')
    list_filter = ('type', 'key', 'slug', 'assignee', 'reporter', 'priority', 'status')