from decouple import config
from django.contrib import admin
from django.core.mail import send_mail

from .models import Parcel, Issue, Address, Receiver


# Register your models here.

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['country', 'city', 'street', 'zip', ]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)


@admin.register(Receiver)
class ReceiverAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', ]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)


class IssueInline(admin.TabularInline):
    model = Issue


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ['category', 'status', 'parcel', ]
    readonly_fields = ['parcel', 'message', ]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)


@admin.register(Parcel)
class ParcelAdmin(admin.ModelAdmin):
    list_display = ['id', 'status']
    readonly_fields = ['pickup_address', 'receiver', 'booked_by', ]
    inlines = [
        IssueInline,
    ]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if change:
            message = f"You are receiving this email because you have a parcel at {request.META['HTTP_HOST']}."

            if 'status' in form.changed_data:
                message += f"\n\nYour parcel has been {obj.status}."

            if 'delivery_agent' in form.changed_data:
                message += f"\n\nDelivery agent {obj.delivery_agent.get_full_name()} has been assigned to your parcel."

            message += f"Please visit our website to know more." + \
                       f"\n\nYour parcel tracking ID, in case you’ve forgotten: {obj.id}" + \
                       f"\n\nThanks for using our service!" + \
                       f"\n\nThe {request.META['HTTP_HOST']} team"

            send_mail(
                subject='Parcel Update',
                message=message,
                from_email=config('EMAIL'),
                recipient_list=[obj.booked_by.email],
            )
