from django.contrib import admin

from .models import Customer, DeliveryAgent


# Register your models here.


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id']
    exclude = ['password', ]
    readonly_fields = ['last_login', 'date_joined', ]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)


@admin.register(DeliveryAgent)
class DeliveryAgentAdmin(admin.ModelAdmin):
    list_display = ['id']
    exclude = ['password', ]
    readonly_fields = ['last_login', 'date_joined', ]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
