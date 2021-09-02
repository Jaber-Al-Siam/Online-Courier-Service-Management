from django.contrib import admin
from jobs.models import Job

# Register your models here.


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'type', ]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
