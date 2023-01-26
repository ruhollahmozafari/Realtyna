from .models import Room, ListingOwner, Booking
from django_filters import rest_framework as filters

class RoomFilters(filters.FilterSet):
    #TODO: add more filter options, now are just main fields 
    listing_owner = filters.CharFilter(field_name="listing_owner", lookup_expr='id')
    price_lte= filters.CharFilter(field_name="price", lookup_expr='lte') # price__lte : 100 
    price_gte= filters.CharFilter(field_name="price", lookup_expr='gte') # price_gte : 200
    lessor = filters.CharFilter(field_name="lessor",) # id of lessor
    id = filters.CharFilter(field_name = 'id', lookup_expr='in')

    class Meta:
        model = Room
        fields = ['id', 'lessor', 'listing_owner',]

class BookingFilters(filters.FilterSet):
    #TODO: add more filter options, now are just main fields 
    listing_owner = filters.CharFilter(field_name="listing_owner", lookup_expr='id')
    guest = filters.CharFilter(field_name="guest", lookup_expr='id')
    room= filters.CharFilter(field_name="room", lookup_expr='id')
    id = filters.CharFilter(field_name = 'id', lookup_expr='in')

    class Meta:
        model = Booking
        fields = ['id', 'listing_owner', 'guest', 'room' ]


