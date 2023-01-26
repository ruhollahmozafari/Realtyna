from django.db import models
from datetime import timedelta, datetime
from django.core.validators import RegexValidator


# phone regex validation
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                message="Phone number must be entered in the format: '+999999999'.\
                                Up to 15 digits allowed.")


class Guest(models.Model):
    """Guest model"""
    name  = models.CharField(max_length=20, help_text='guest name', 
                                blank=False, null=False,)
    age   = models.IntegerField(help_text='guest age',
                                blank=True, null=True,)
    phone_number = models.CharField(validators=[phone_regex], 
                                    help_text='guest phone', 
                                    max_length=17, blank=False, 
                                    null = False)
    email = models.EmailField(max_length=30, help_text='guest name',
                                blank=False, null=False)
    
    def __str__(self) -> str:
        return self.name


class Lessor(models.Model):
    """lessor model that contains information of the lessor(landlord or owner)"""
    
    name  = models.CharField(max_length=20, help_text='guest name', 
                                blank=False, null=False,)
    phone_number = models.CharField(validators=[phone_regex], 
                                    help_text='guest phone', 
                                    max_length=17, blank=False, 
                                    null = False)
    email = models.EmailField(max_length=30, help_text='guest name',
                                blank=False, null=False)
    
    def __str__(self) -> str:
        return self.name


class ListingOwner(models.Model):
    """listing owner model, a listing owner can have multipl rooms for reservation"""
    
    name  = models.CharField(max_length=20,
                            help_text='listing owner name', blank=False, null=False,)
    phone_number = models.CharField(validators=[phone_regex], 
                                    help_text='owner phone', 
                                    max_length=17, blank=False, 
                                    null = False)

    email = models.EmailField(max_length=30, 
                                help_text='owner name', blank=False, null=False)
    
    def __str__(self) -> str:
        return self.name


class Room(models.Model):
    """Room model, each room tow connections, one is to a listing owner model and \
        the other to lessor model.guest can contact the lessor to get more information about the rooms.
        """
    listing_owner = models.ForeignKey("booking.ListingOwner",null=True,
                                        on_delete=models.SET_NULL)  
    # title     = models.CharField(max_length=20, help_text='title for room')
    location = models.CharField(max_length=50) #TODO:2 make geo
    lessor   = models.ForeignKey("booking.Lessor",blank=False, null=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=250, blank=False, null=False)
    description = models.TextField()
    price = models.BigIntegerField(help_text='pay for each night')
    #TODO: fields such as number of rooms, bedroom or .... can be add later and used by djagno filters 

    def __str__(self) -> str:
        return str(self.id)


class Booking(models.Model):
    """booking model to save data of each booking instance"""
    
    listing_owner = models.ForeignKey("booking.ListingOwner",null=True, on_delete=models.SET_NULL)
    guest         = models.ForeignKey("booking.Guest",null=True, on_delete=models.SET_NULL)
    room          = models.ForeignKey("booking.Room",null=True, on_delete=models.SET_NULL, related_name='bookings')
    # if no check in set, today and tomorrow will be check in and out
    checkin_date  = models.DateField(blank=False, null=False) 
    checkout_date = models.DateField(blank=False, null=False)
    is_checkout   = models.BooleanField(default=False,)
    # to log the create time and update (logging)
    created       = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated       = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self) -> str:
        return f"{self.room.id} {self.guest.name}" 

    def listin_owner_name(self) -> str:
        return self.listing_owner.name 

    def charge(self) -> float:
        """cacluate the the price of the booking \
            based on the room price and number of days of stay"""
        
        return (self.checkout_date - self.checkin_date + timedelta(1)).days* \
        self.room.price

