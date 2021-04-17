from django.contrib import admin
from .models import Destination, Parcel, Shipping_Update


class ParcelAdmin(admin.ModelAdmin):
    fieldsets = [
        ('',
         {'fields': ['label', 'delivered', 'carrier', 'kind', 'destination', 'items', 'contents', 'weight'], }),
        ('Date information',
         {'fields': ['date_sent', 'date_arrived_port', 'date_sent_port', 'date_arrived_post_office',
                     'date_received_destination'],
          'classes': ['expand']
          }),
        ('Date information',
         {'fields': ['tracking_us', 'tracking_international'],
          'classes': ['expand']
          }),
    ]
    list_display = ['label', 'weight', 'kind', 'date_sent', 'tracking_us', 'tracking_international', 'delivered']
    list_filter = ['weight', 'kind', 'date_sent']
    search_fields = ['label', 'tracking_us', 'tracking_international']


class DestinationAdmin(admin.ModelAdmin):
    list_display = ['address_label']


admin.site.register(Destination, DestinationAdmin)
admin.site.register(Parcel, ParcelAdmin)
admin.site.register(Shipping_Update)
# Register your models here.
