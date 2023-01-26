from django.contrib import admin
from .models import (Guest,
                     Lessor,
                     Room,
                     ListingOwner,
                     Booking,)

class BookingAdmin(admin.ModelAdmin):
    list_display  = ['id','room', 'listing_owner', 'guest', 'checkin_date', 'checkout_date']


class RoomAdmin(admin.ModelAdmin):
    list_display  = ['id', 'listing_owner', 'lessor', 'price']

#TODO: complete admin panel

admin.site.register(Booking, BookingAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Guest)
admin.site.register(Lessor)
admin.site.register(ListingOwner)


