from django.contrib import admin, messages
from django.core.mail import send_mail
from django.utils.translation import ngettext
from .models import Parcel

# Register your models here.


@admin.register(Parcel)
class ParcelAdmin(admin.ModelAdmin):
    list_display = ['id', 'status']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        send_mail(
            subject=request.POST['type'],
            message='Your parcel status has been changed to ' + request.POST['status'],
            from_email='jaberalsiam@gmail.com',
            recipient_list=[obj.email],
        )

    def make_published(self, request, queryset):
        updated = queryset.update(status='processing')
        self.message_user(request, ngettext(
            '%d story was successfully marked as published.',
            '%d stories were successfully marked as published.',
            updated,
        ) % updated, messages.SUCCESS)
