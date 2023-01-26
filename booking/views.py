from .models import (Room,
                     ListingOwner,
                     Guest,
                     Booking,
                     Lessor,
                     )
from .serializers import (RoomSerializer, 
                         ListingOwnerSerializer, 
                         GuestSerializer,
                         LessorSerializer,
                         BookingSerializerCreate,
                         BookingNestedSerializerShow,
                         RoomNestedSerializer,
                         )

from rest_framework.generics import ListAPIView, RetrieveAPIView
from .filters import RoomFilters, BookingFilters

class RoomListView(ListAPIView):
    serializer_class = RoomSerializer
    filterset_class = RoomFilters 
    queryset = Room.objects.filter()

class RoomAvailability(ListAPIView):
    """api to filter all available rooms in a specific date by excluding booking for room in that day"""
    serializer_class = RoomSerializer
    filterset_class = RoomFilters
    # queryset = Room.objects.filter()
    
    def get_queryset(self):
        """use the booking model to exclude the rooms that are booked in that date
        these also return number of rooms in response,"""
        qr = Room.objects.prefetch_related('bookings').exclude(
            bookings__checkin_date__lte = self.kwargs.get('date'), 
            bookings__checkout_date__gt = self.kwargs.get('date'))
        return qr 


class RoomRetriveView(RetrieveAPIView):
    serializer_class = RoomNestedSerializer
    # pagination_class = None
    model = Room
    queryset = Room.objects.select_related(
                            'listing_owner', 'lessor',
                            ).filter()


class ListingOwnersRetriveView(ListAPIView):
    serializer_class = ListingOwnerSerializer
    # filterset_class = TempUserFilters
    queryset = ListingOwner.objects.filter()
    

class LessorsRetriveView(ListAPIView):
    serializer_class = LessorSerializer
    # filterset_class = TempUserFilters
    queryset = Lessor.objects.filter()


class BookingRetriveView(ListAPIView):
    serializer_class = BookingNestedSerializerShow
    filterset_class = BookingFilters
    queryset = Booking.objects.select_related(
                                'room', 'guest', 'listing_owner'
                                ).filter()#TODO: use django debug
    

class GuestRetriveView(ListAPIView):
    serializer_class = GuestSerializer
    queryset = Guest.objects.filter()
    

