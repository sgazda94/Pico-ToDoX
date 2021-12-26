from django.contrib import admin

# Register your models here.
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    pass


admin.site.register(Task, TaskAdmin)