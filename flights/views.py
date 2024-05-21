from django.shortcuts import render
from .models import Flight

def search_flights(request):
    flights = Flight.objects.all()
    return render(request, 'flights/search_flights.html', {'flights': flights})

from django.shortcuts import render
from .models import Flight
from .forms import FlightSearchForm

def search_flights(request):
    if request.method == "POST":
        form = FlightSearchForm(request.POST)
        if form.is_valid():
            departure_airport = form.cleaned_data['departure_airport']
            arrival_airport = form.cleaned_data['arrival_airport']
            departure_date = form.cleaned_data['departure_date']
            flights = Flight.objects.filter(
                departure_airport=departure_airport,
                arrival_airport=arrival_airport,
                departure_time__date=departure_date
            )
            return render(request, 'flights/search_results.html', {'flights': flights})
    else:
        form = FlightSearchForm()
    return render(request, 'flights/search_flights.html', {'form': form})

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .models import Flight, Booking

@login_required
def book_flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    Booking.objects.create(user=request.user, flight=flight, status='Confirmed')
    return redirect


from django.db import models
from django.contrib.auth.models import User

# class Booking(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
#     booking_date = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=20, default='Pending')

def __str__(self):
        return f"{self.user.username} - {self.flight.flight_number} - {self.status}"


from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Flight, Booking

@login_required
def book_flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    Booking.objects.create(user=request.user, flight=flight, status='Confirmed')
    return redirect('payment:success')


from django.shortcuts import render
from .models import Flight

def search_flights(request):
    flights = Flight.objects.all()
    return render(request, 'flights/search_results.html', {'flights': flights})
