"""Tests for bookins/views.py module"""
import datetime as dt
from model_bakery import baker
from rest_framework.test import APITestCase
from django.conf import settings





class TestGuestListView(APITestCase):
    """ Test Guest List View"""
    def setUp(self) -> None:
        
        """SetUp test data"""
        self.url ="/booking/guests/"

        # create a guest
        self.guest = baker.make(
            "booking.Guest",
        )
        self.guest.save()

    
    def test_guest_list(self):
        """Test if the list api works fine"""
        response = self.client.get(self.url,)
        self.assertEqual(200, response.status_code)
        self.assertIn("results", response.data)


class TestLessorListView(APITestCase):
    """ Test Lessor List View"""
    def setUp(self) -> None:
            
        """SetUp test data"""
        self.url ="/booking/lessors/"

        # create a guest
        self.guest = baker.make(
            "booking.Lessor",
        )
        self.guest.save()

    def test_lessor_list(self):
        """Test if the list api works fine"""
        response = self.client.get(self.url,)
        self.assertEqual(200, response.status_code)
        self.assertIn("results", response.data)


class TestListingOwnerListView(APITestCase ):
    """ Test ListingOwner List View"""
    def setUp(self) -> None:
            
        """SetUp test data"""
        self.url ="/booking/listing_owners/"

        # create a guest
        self.guest = baker.make(
            "booking.ListingOwner",
        )
        self.guest.save()

    def test_listin_owner_list(self):
        """Test if the list api works fine"""
        response = self.client.get(self.url,)
        self.assertEqual(200, response.status_code)
        self.assertIn("results", response.data)


class TestRoomListView(APITestCase):
    """ Test Room List View"""
    print('starting the tests')
    
    def setUp(self) -> None:
        
        """SetUp test data"""
        self.url ="/booking/rooms/"

        # create a guest
        self.guest = baker.make(
            "booking.Guest",
        )
        self.guest.save()
        
        # create a lessor
        self.lessor = baker.make(
            "booking.Lessor",
        )
        self.lessor.save()
        
        # create a listing owner
        self.lising_owner = baker.make(
            "booking.ListingOwner",
        )
        self.lising_owner.save()

        # create Rooms
        self.guest = baker.make(
            "booking.Room",
            listing_owner=self.lising_owner,
            location = 'NY',
            lessor = self.lessor,
            address = 'No. 1, first street, Tehran,',
            description = 'nice room',
            price = 100,
        )
        self.guest.save()

    def test_room_list(self):
        """check if list api works fine"""
        response = self.client.get(self.url,)
        self.assertEqual(200, response.status_code)
        self.assertEqual('NY', response.data['results'][0]['location'])
        self.assertIn("results", response.data)
        

class TestBookingListView(APITestCase):
    """ Test Booking List View"""
    
    def setUp(self) -> None:
        
        """SetUp test data"""
        self.url ="/booking/"

        # create a guest
        self.guest = baker.make(
            "booking.Guest",
        )
        self.guest.save()
        
        # create a lessor
        self.lessor = baker.make(
            "booking.Lessor",
        )
        self.lessor.save()
        
        # create a listing owner
        self.lising_owner = baker.make(
            "booking.ListingOwner",
        )
        self.lising_owner.save()

        # create Rooms
        self.room = baker.make(
            "booking.Room",
            listing_owner=self.lising_owner,
            location = 'NY',
            lessor = self.lessor,
            address = 'No. 1, first street, Tehran,',
            description = 'nice room',
            price = 100,
        )
        self.room.save()
        
        # create bookings
        self.booking = baker.make(
            "booking.Booking",
            checkin_date= '2023-01-27',
            checkout_date= '2023-01-28',
            room = self.room,
            guest = self.guest,
        )
        
        self.booking.save()
        

    def test_room_list(self):
        """check if list api works fine"""
        response = self.client.get(self.url,)
        self.assertEqual(200, response.status_code)
        self.assertIn("results", response.data)
        


class TestBookingCreateView(APITestCase):
    """ Test Booking Create View"""
    
    def setUp(self) -> None:
        
        """SetUp test data"""
        self.url ="/booking/set/"

        # create a guest
        self.guest = baker.make(
            "booking.Guest",
        )
        self.guest.save()
        
        # create a lessor
        self.lessor = baker.make(
            "booking.Lessor",
        )
        self.lessor.save()
        
        # create a listing owner
        self.lising_owner = baker.make(
            "booking.ListingOwner",
        )
        self.lising_owner.save()

        # create Rooms
        self.room = baker.make(
            "booking.Room",
            listing_owner=self.lising_owner,
            location = 'NY',
            lessor = self.lessor,
            address = 'No. 1, first street, Tehran,',
            description = 'nice room',
            price = 100,
        )
        self.room.save()
        

    def test_room_create(self):
        """check if list api works fine"""
        data ={
            "checkin_date": '2023-02-02',
            "checkout_date": '2023-02-04',
            "room" : self.room.id,
            "guest" : self.guest.id,
        }
        
        response = self.client.post(self.url,data= data)
        self.assertEqual(201, response.status_code)



class TestRoomAvailabilityView(APITestCase):
    """ Test Room Availability View"""
    
    def setUp(self) -> None:
        
        """SetUp test data"""
        self.url ="/booking/availability/{}/"

        # create a guest
        self.guest = baker.make(
            "booking.Guest",
        )
        self.guest.save()
        
        # create a lessor
        self.lessor = baker.make(
            "booking.Lessor",
        )
        self.lessor.save()
        
        # create a listing owner
        self.lising_owner = baker.make(
            "booking.ListingOwner",
        )
        self.lising_owner.save()

        # create Rooms
        self.room = baker.make(
            "booking.Room",
            listing_owner=self.lising_owner,
            location = 'NY',
            lessor = self.lessor,
            address = 'No. 1, first street, Tehran,',
            description = 'nice room',
            price = 100,
        )
        self.room.save()
        

    def test_room_list(self):
        """check if room availability is working fine or not"""
        date = dt.date.today()
        response = self.client.get(self.url.format(date))
        self.assertEqual(200, response.status_code)
        self.assertIn("results", response.data)
    