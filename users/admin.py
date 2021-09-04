from django.contrib import admin

from parcels.models import Parcel
from .models import Customer, DeliveryAgent


# Register your models here.

class CustomerParcelInline(admin.TabularInline):
    model = Parcel
    fk_name = 'booked_by'


class DeliveryAgentParcel(admin.TabularInline):
    model = Parcel
    fk_name = 'delivery_agent'


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['email']
    exclude = ['password', ]
    readonly_fields = ['last_login', 'date_joined', ]
    inlines = [
        CustomerParcelInline
    ]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)


@admin.register(DeliveryAgent)
class DeliveryAgentAdmin(admin.ModelAdmin):
    list_display = ['id']
    exclude = ['password', ]
    readonly_fields = ['last_login', 'date_joined', ]
    inlines = [
        DeliveryAgentParcel
    ]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
