from rest_framework.serializers import ModelSerializer
from .models import (Room,
                     ListingOwner,
                     Guest,
                     Booking,
                     Lessor,
                     )


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
    listing_owner = ListingOwnerSerializer()
    
    class Meta:
        model = Booking
        fields = '__all__'


class BookingSerializerCreate(ModelSerializer):
    """serilaizer for createing booking instances"""
    class Meta:
        model = Booking
        fields = '__all__'

    

