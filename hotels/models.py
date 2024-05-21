# from django.db import models
# from django.contrib.auth.models import User


# class Hotel(models.Model):
#     name = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
#     address = models.CharField(max_length=200)
#     price_per_night = models.DecimalField(max_digits=10, decimal_places=2)

# class Room(models.Model):
#     hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
#     room_type = models.CharField(max_length=50)
#     number_of_rooms = models.IntegerField()
#     price_per_night = models.DecimalField(max_digits=10, decimal_places=2)

# class Booking(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
#     check_in_date = models.DateField()
#     check_out_date = models.DateField()
#     booking_date = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=20, default='Pending')
    
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hotel_bookings')


# # from django.db import models
# # from django.contrib.auth.models import User

# # class Booking(models.Model):
# #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# #     hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
# #     check_in_date = models.DateField()
# #     check_out_date = models.DateField()
# #     booking_date = models.DateTimeField(auto_now_add=True)
# #     status = models.CharField(max_length=20, default='Pending')

#     def __str__(self):
#         return f"{self.user.username} - {self.hotel.name} - {self.status}"


# from django.db import models
# from django.contrib.auth.models import User

# class Hotel(models.Model):
#     name = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
#     price_per_night = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return self.name

# # class Booking(models.Model):
# #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# #     hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
# #     check_in_date = models.DateField()
# #     check_out_date = models.DateField()
# #     booking_date = models.DateTimeField(auto_now_add=True)
# #     status = models.CharField(max_length=20, default='Pending')

#     def __str__(self):
#         return f"{self.user.username} - {self.hotel.name} - {self.status}"



# from django.db import models

# # Define the Hotel model
# class Hotel(models.Model):
#     name = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
#     # Other fields...

#     def __str__(self):
#         return self.name

# # Define the Booking model
# class Booking(models.Model):
#     hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
#     # Other fields...

# # Define the Room model
# class Room(models.Model):
#     hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
#     # Other fields...


from django.db import models
from django.contrib.auth.models import User

# class Hotel(models.Model):
#     name = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
#     price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.TextField()
# models.py


# class Hotel(models.Model):
#     name = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#     country = models.CharField(max_length=255)
#     price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
#     # other fields...
# models.py
# from django.db import models

# class Hotel(models.Model):
#     name = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#     country = models.CharField(max_length=255)
#     price_per_night = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Set your desired default value
#     # other fields...
from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other fields as necessary

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.user.username} - {self.hotel.name} - {self.status}"



# models.py
