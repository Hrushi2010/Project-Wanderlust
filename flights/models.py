from django.contrib.auth.models import User

from django.db import models

class Airport(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

# class Flight(models.Model):
#     flight_number = models.CharField(max_length=10)
#     departure_airport = models.ForeignKey(Airport, related_name='departure_airport', on_delete=models.CASCADE)
#     arrival_airport = models.ForeignKey(Airport, related_name='arrival_airport', on_delete=models.CASCADE)
#     departure_time = models.DateTimeField()
#     arrival_time = models.DateTimeField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)


# class Booking(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
#     booking_date = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=20, default='Pending')


from django.db import models
from django.contrib.auth.models import User

class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    departure_airport = models.CharField(max_length=100)
    arrival_airport = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.flight_number} from {self.departure_airport} to {self.arrival_airport}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='flight_bookings')

    def __str__(self):
        return f"{self.user.username} - {self.flight.flight_number} - {self.status}"




