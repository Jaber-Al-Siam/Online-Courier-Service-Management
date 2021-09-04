from django.contrib import admin
from django.core.mail import send_mail
from .models import Parcel

# Register your models here.


@admin.register(Parcel)
class ParcelAdmin(admin.ModelAdmin):
    list_display = ['id', 'status']
    readonly_fields = ['pickup_address', 'receiver', 'booked_by', ]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        send_mail(
            subject=request.POST['type'],
            message='Your parcel status has been changed to ' + request.POST['status'],
            from_email='jaberalsiam@gmail.com',
            recipient_list=[obj.email],
        )
