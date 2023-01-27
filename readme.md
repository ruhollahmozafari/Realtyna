# Django Rest Project for booking rooms. 

You can check the endpoint by going to `localhost:8000/swagger/`. there are description and you can test them.

## Description:
As a listing owner, I want a system for making and tracking reservations that can be handled by third-party services.

* The system can be used by multiple listings.
* The system provides REST API endpoints:
-> To make reservations
-> To check if a number of rooms are available at a certain time
* A reservation is for a name (any string) and for a certain amount of time
* The listing owner can get an overview over the booked rooms as an HTML or TEXT report


Limitations:

* Authentication / Authorization is not in the scope of this task
* No localization needed
## Test 
The directory `booking/tests` contains test and it assure the reservation process and all the api are working properly.  

## Docker
there a docker file  and you can deplopyu the project by running command `docker build --tag realtyna .`  and run container by `docker run -d realtyna`


note that project was large but since I wanted stick to the 8-hour deadline, I tried to do my best in that short amount of time.






