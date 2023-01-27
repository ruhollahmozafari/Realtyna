from django.contrib import admin
from django.urls import path
from .views import (RoomListView,
                    ListingOwnersRetriveView,
                    LessorsRetriveView,
                    BookingRetriveView,
                    RoomRetriveView,
                    GuestRetriveView,
                    RoomAvailability,
                    BookingCreateView,
                    )

urlpatterns = [
    path('rooms/', RoomListView.as_view(), name = 'rooms_list'),
    path('bookings/', BookingRetriveView.as_view(), name = 'booking_list'),
    path('lessors/', LessorsRetriveView.as_view(), name = 'lessor_list'),
    path('listing_owners/', ListingOwnersRetriveView.as_view(), name = 'rooms_list'),
    path('rooms/<int:pk>/', RoomRetriveView.as_view(), name = 'room_retrieve'),
    path('guests/', GuestRetriveView.as_view(), name = 'guest_list'),
    path('availability/<str:date>/', RoomAvailability.as_view(), name = 'rooms_availability'),
    path('set/', BookingCreateView.as_view(), name = 'set_booking'),
    
]
