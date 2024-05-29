# from django.contrib.auth.models import User

# from django.db import models

# class Airport(models.Model):
#     name = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)

# # class Flight(models.Model):
# #     flight_number = models.CharField(max_length=10)
# #     departure_airport = models.ForeignKey(Airport, related_name='departure_airport', on_delete=models.CASCADE)
# #     arrival_airport = models.ForeignKey(Airport, related_name='arrival_airport', on_delete=models.CASCADE)
# #     departure_time = models.DateTimeField()
# #     arrival_time = models.DateTimeField()
# #     price = models.DecimalField(max_digits=10, decimal_places=2)


# # class Booking(models.Model):
# #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# #     flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
# #     booking_date = models.DateTimeField(auto_now_add=True)
# #     status = models.CharField(max_length=20, default='Pending')


# from django.db import models
# from django.contrib.auth.models import User

# class Flight(models.Model):
#     flight_number = models.CharField(max_length=10)
#     departure_airport = models.CharField(max_length=100)
#     arrival_airport = models.CharField(max_length=100)
#     departure_time = models.DateTimeField()
#     arrival_time = models.DateTimeField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"{self.flight_number} from {self.departure_airport} to {self.arrival_airport}"

# class Booking(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
#     booking_date = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=20, default='Pending')
    
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='flight_bookings')

#     def __str__(self):
#         return f"{self.user.username} - {self.flight.flight_number} - {self.status}"


# flights/models.py

# from django.db import models

# class Flight(models.Model):
#     flight_number = models.CharField(max_length=10)
#     departure_airport = models.CharField(max_length=50)
#     arrival_airport = models.CharField(max_length=50)
#     departure_time = models.DateTimeField()
#     arrival_time = models.DateTimeField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"{self.flight_number} from {self.departure_airport} to {self.arrival_airport}"

# # class Booking(models.Model):
# #     flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
# #     passenger_name = models.CharField(max_length=100)
# #     passenger_email = models.EmailField()
# #     booking_date = models.DateTimeField(auto_now_add=True)
# #     amount_paid = models.DecimalField(max_digits=10, decimal_places=2)

# #     def __str__(self):
# #         return f"Booking for {self.passenger_name} on flight {self.flight.flight_number}"


# # flights/models.py

# # from django.db import models

# # class Booking(models.Model):
# #     flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
# #     passenger_name = models.CharField(max_length=100)
# #     passenger_email = models.EmailField(default='default@example.com')
# #     booking_date = models.DateTimeField(auto_now_add=True)
# #     check_in_date = models.DateTimeField(null=True, blank=True)
# #     amount = models.DecimalField(max_digits=10, decimal_places=2)

# #     def __str__(self):
# #         return f"{self.passenger_name} - {self.flight.flight_number}"


# # flights/models.py

# from django.db import models

# class Booking(models.Model):
#     flight = models.ForeignKey('Flight', on_delete=models.CASCADE)
#     passenger_name = models.CharField(max_length=100, default='Default Name')
#     passenger_email = models.EmailField(default='default@example.com')
#     booking_date = models.DateTimeField(auto_now_add=True)
#     check_in_date = models.DateTimeField(null=True, blank=True)
#     amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

#     def __str__(self):
#         return f"{self.passenger_name} - {self.flight.flight_number}"


# flights/models.py

from django.db import models

class Airport(models.Model):
    code = models.CharField(max_length=3, unique=True)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.flight_number} from {self.departure_airport} to {self.arrival_airport}"

class Booking(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=100)
    booking_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Booking for {self.passenger_name} on flight {self.flight}"
