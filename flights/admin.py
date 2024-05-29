from django.contrib import admin

# Register your models here.
# flights/admin.py
from django.contrib import admin
from .models import Flight, Booking  # Import your models here

# Register your models here
admin.site.register(Flight)
admin.site.register(Booking)
