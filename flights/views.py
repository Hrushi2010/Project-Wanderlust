# # from django.shortcuts import render
# # from .models import Flight

# # def search_flights(request):
# #     flights = Flight.objects.all()
# #     return render(request, 'flights/search_flights.html', {'flights': flights})

# # from django.shortcuts import render
# # from .models import Flight
# # from .forms import FlightSearchForm

# # def search_flights(request):
# #     if request.method == "POST":
# #         form = FlightSearchForm(request.POST)
# #         if form.is_valid():
# #             departure_airport = form.cleaned_data['departure_airport']
# #             arrival_airport = form.cleaned_data['arrival_airport']
# #             departure_date = form.cleaned_data['departure_date']
# #             flights = Flight.objects.filter(
# #                 departure_airport=departure_airport,
# #                 arrival_airport=arrival_airport,
# #                 departure_time__date=departure_date
# #             )
# #             return render(request, 'flights/search_results.html', {'flights': flights})
# #     else:
# #         form = FlightSearchForm()
# #     return render(request, 'flights/search_flights.html', {'form': form})

# # from django.contrib.auth.decorators import login_required
# # from django.shortcuts import get_object_or_404, redirect
# # from .models import Flight, Booking

# # @login_required
# # def book_flight(request, flight_id):
# #     flight = get_object_or_404(Flight, id=flight_id)
# #     Booking.objects.create(user=request.user, flight=flight, status='Confirmed')
# #     return redirect


# # from django.db import models
# # from django.contrib.auth.models import User

# # # class Booking(models.Model):
# # #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# # #     flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
# # #     booking_date = models.DateTimeField(auto_now_add=True)
# # #     status = models.CharField(max_length=20, default='Pending')

# # def __str__(self):
# #         return f"{self.user.username} - {self.flight.flight_number} - {self.status}"


# # from django.contrib.auth.decorators import login_required
# # from django.shortcuts import get_object_or_404, redirect, render
# # from .models import Flight, Booking

# # @login_required
# # def book_flight(request, flight_id):
# #     flight = get_object_or_404(Flight, id=flight_id)
# #     Booking.objects.create(user=request.user, flight=flight, status='Confirmed')
# #     return redirect('payment:success')


# # from django.shortcuts import render
# # from .models import Flight

# # def search_flights(request):
# #     flights = Flight.objects.all()
# #     return render(request, 'flights/search_results.html', {'flights': flights})


# # flights/views.py

# # from django.shortcuts import render, get_object_or_404, redirect
# # from django.urls import reverse
# # from .models import Flight, Booking
# # from .forms import FlightSearchForm, BookingForm

# # def search_flights(request):
# #     if request.method == 'POST':
# #         form = FlightSearchForm(request.POST)
# #         if form.is_valid():
# #             departure_airport = form.cleaned_data['departure_airport']
# #             arrival_airport = form.cleaned_data['arrival_airport']
# #             flights = Flight.objects.filter(departure_airport=departure_airport, arrival_airport=arrival_airport)
# #             return render(request, 'flights/search_results.html', {'flights': flights})
# #     else:
# #         form = FlightSearchForm()
# #     return render(request, 'flights/search_flights.html', {'form': form})

# # def book_flight(request, flight_id):
# #     flight = get_object_or_404(Flight, pk=flight_id)
# #     if request.method == 'POST':
# #         form = BookingForm(request.POST)
# #         if form.is_valid():
# #             booking = form.save(commit=False)
# #             booking.amount_paid = flight.price
# #             booking.save()
# #             return redirect('booking_confirmation', booking_id=booking.id)
# #     else:
# #         form = BookingForm(initial={'flight': flight})
# #     return render(request, 'flights/book_flight.html', {'form': form, 'flight': flight})

# # def booking_confirmation(request, booking_id):
# #     booking = get_object_or_404(Booking, pk=booking_id)
# #     return render(request, 'flights/booking_confirmation.html', {'booking': booking})

# # def cancel_booking(request, booking_id):
# #     booking = get_object_or_404(Booking, pk=booking_id)
# #     if request.method == 'POST':
# #         booking.delete()
# #         return redirect('search_flights')
# #     return render(request, 'flights/cancel_booking.html', {'booking': booking})


# # flights/views.py

# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Flight, Booking
# from .forms import SearchForm, BookingForm

# def flight_list(request):
#     flights = Flight.objects.all()
#     return render(request, 'flights/flight_list.html', {'flights': flights})

# def search_flights(request):
#     if request.method == 'POST':
#         form = SearchForm(request.POST)
#         if form.is_valid():
#             flights = Flight.objects.filter(
#                 departure_airport=form.cleaned_data['departure_airport'],
#                 arrival_airport=form.cleaned_data['arrival_airport'],
#                 departure_date=form.cleaned_data['departure_date']
#             )
#             return render(request, 'flights/flight_list.html', {'flights': flights})
#     else:
#         form = SearchForm()
#     return render(request, 'flights/search_flights.html', {'form': form})

# def book_flight(request, flight_id):
#     flight = get_object_or_404(Flight, id=flight_id)
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             booking = form.save(commit=False)
#             booking.flight = flight
#             booking.save()
#             return redirect('flights:flight_list')
#     else:
#         form = BookingForm()
#     return render(request, 'flights/book_flight.html', {'form': form, 'flight': flight})

# def cancel_booking(request, booking_id):
#     booking = get_object_or_404(Booking, id=booking_id)
#     booking.delete()
#     return redirect('flights:flight_list')

# # flights/views.py
# from django.shortcuts import render
# from .models import Flight

# def flight_list(request):
#     flights = Flight.objects.all()
#     return render(request, 'flights/flight_list.html', {'flights': flights})


# views.py
# from django.shortcuts import render
# from django.shortcuts import render

# def flight_list(request):
#     return render(request, 'flights/flight_list.html')

# from .api_client import create_search_session, poll_search_results

# def search_flights_view(request):
#     if request.method == "POST":
#         origin = request.POST.get('origin')
#         destination = request.POST.get('destination')
#         departure_date = request.POST.get('departure_date')
#         return_date = request.POST.get('return_date')
#         session_token = create_search_session(origin, destination, departure_date, return_date)
#         if session_token:
#             flights = poll_search_results(session_token)
#             return render(request, 'flights/search_results.html', {'flights': flights['itineraries']})
#     return render(request, 'flights/search_form.html')


# from django.shortcuts import render
# from .api_client import create_search_session, poll_search_results

# def search_flights_view(request):
#     if request.method == "POST":
#         origin = request.POST.get('origin')
#         destination = request.POST.get('destination')
#         departure_date = request.POST.get('departure_date')
#         return_date = request.POST.get('return_date')
#         session_token = create_search_session(origin, destination, departure_date, return_date)
#         if session_token:
#             flights = poll_search_results(session_token)
#             return render(request, 'flights/search_results.html', {'flights': flights['itineraries']})
#     return render(request, 'flights/search_form.html')


# flights/views.py
# from django.shortcuts import render

# def flight_list(request):
#     return render(request, 'flights/flight_list.html')

# def search_flights_view(request):
#     if request.method == "POST":
#         origin = request.POST.get('origin')
#         destination = request.POST.get('destination')
#         departure_date = request.POST.get('departure_date')
#         return_date = request.POST.get('return_date')
#         # Implement API call and result handling here
#         flights = []  # Replace with actual data
#         return render(request, 'flights/search_results.html', {'flights': flights})
#     return render(request, 'flights/search_form.html')


# flights/views.py
# from django.shortcuts import render

# def flight_list(request):
#     return render(request, 'flights/flight_list.html')

# def search_flights_view(request):
#     if request.method == "POST":
#         origin = request.POST.get('origin')
#         destination = request.POST.get('destination')
#         departure_date = request.POST.get('departure_date')
#         return_date = request.POST.get('return_date')
#         # Implement API call and result handling here
#         flights = []  # Replace with actual data
#         return render(request, 'flights/search_results.html', {'flights': flights})
#     return render(request, 'flights/search_form.html')

# flights/views.py
from django.conf import settings
# flights/views.py
from django.shortcuts import render

def flight_list(request):
    return render(request, 'flights/flight_list.html')


def search_flights_view(request):
    if request.method == "POST":
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        departure_date = request.POST.get('departure_date')
        return_date = request.POST.get('return_date')

        api_url = "https://api.example.com/flights"
        params = {
            "origin": origin,
            "destination": destination,
            "departure_date": departure_date,
            "return_date": return_date,
            "api_key": settings.API_KEY
        }

        response = requests.get(api_url, params=params)
        
        if response.status_code == 200:
            flights = response.json().get('flights', [])
        else:
            flights = []

        return render(request, 'flights/search_results.html', {'flights': flights})

    return render(request, 'flights/search_form.html')
