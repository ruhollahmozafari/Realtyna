from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import (Room,
                     ListingOwner,
                     Guest,
                     Booking,
                     Lessor,
                     )
import datetime as dt
from django.db.models import Q
from icecream  import ic

class GuestSerializer(ModelSerializer):
    
    class Meta:
        model = Guest
        fields = '__all__'

class ListingOwnerSerializer(ModelSerializer):
    
    class Meta:
        model = ListingOwner
        fields = '__all__'


class LessorSerializer(ModelSerializer):
    
    class Meta:
        model = Lessor
        fields = '__all__'
        

class RoomSerializer(ModelSerializer):
    
    class Meta:
        model = Room
        fields = '__all__'
        
        
class RoomNestedSerializer(ModelSerializer):
    listing_owner = ListingOwnerSerializer()
    lessor = LessorSerializer()
    
    class Meta:
        model = Room
        fields = '__all__'
        

class BookingNestedSerializerShow(ModelSerializer):
    """nested serilaizer for shwoing booking instances"""
    room = RoomSerializer()
    guest = GuestSerializer()
    
    class Meta:
        model = Booking
        fields = '__all__'


class BookingCreateSerializer(ModelSerializer):
    """serilaizer for createing booking instances"""
    class Meta:
        model = Booking
        fields = '__all__'
        extra_kwargs = {
                "guest": {"required": True, "allow_null": False, },
                "room": {"required": True, "allow_null": False},
                "checkin_date": {"required": True, "allow_null": False},
                "checkout_date": {"required": True, "allow_null": False},
                }
        
    
    def validate(self, data):   
        """Check that the checkin date is before the checkout date."""
        
        # check-in is before check-out 
        if data['checkin_date'] >= data['checkout_date']:
            raise serializers.ValidationError(
                {"checkout_date": "check-in must be before check-out"})
        #check-in is after than today
        #so guest can only book a room for todays and after
        if data['checkin_date'] < dt.date.today():
            raise serializers.ValidationError(
                {"checkin_date": "check-in can not be before today"})
        
        # check if a that room is booked in that day or not\
            # by checking if two checkin and checkout overlaps or not
        if Room.objects.prefetch_related('bookings').filter(
                    Q(bookings__checkin_date__range = [data['checkin_date'],data['checkout_date']])|
                    Q(bookings__checkout_date__range = [data['checkin_date'],data['checkout_date']]),
                    ).exists():
            raise serializers.ValidationError(
                {"checkin_date": "the room is not available in this date and has been booked."})
        
        # and if all good
        return data


