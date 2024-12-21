# Register your models here.
# tasks/admin.py

from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'due_date', 'created_at')
    list_filter = ('status', 'due_date', 'assignees')
    search_fields = ('title', 'description')
    filter_horizontal = ('assignees',)