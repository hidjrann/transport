from django.contrib import admin
from .models import Booking, Car, Ride
# Register your models here.

admin.site.register(Car)

@admin.register(Booking)
class Bookadmin(admin.ModelAdmin):
    list_display = ['customer_name', 'booking_start_date', 'booking_end_date', 'is_approved']
    list_filter = ['is_approved']
    search_fields = ['customer_name']
    list_editable = ['is_approved']

    actions = ['email_customers']
    def email_customers(self, request, queryset):
        for booking in queryset:
            if booking.is_approved:
                email_body = f'Dear {booking.customer_name},We are pleased to inform you that your booking has been approved. Thanks'
            else:
                email_body = f'Dear {booking.customer_name},Unfortunately we do not have the capacity right now to accept your booking. Thanks'
            print(email_body)

        self.message_user(request, 'Emails were send successfully')    
    email_customers.short_description = 'Send email about booking status to customers'




admin.site.site_header = 'U-Transport--admin'                    # default: "Django Administration"
admin.site.index_title = 'U-transport'                 # default: "Site administration"
admin.site.site_title = 'admin' # default: "Django site admin"


from mapbox_location_field.admin import MapAdmin

admin.site.register(Ride, MapAdmin)