# from django.shortcuts import render
# from .models import Hotel

# def search_hotels(request):
#     hotels = Hotel.objects.all()
#     return render(request, 'hotels/search_hotels.html', {'hotels': hotels})


# from django.shortcuts import render
# from .models import Hotel
# from .forms import HotelSearchForm

# def search_hotels(request):
#     if request.method == "POST":
#         form = HotelSearchForm(request.POST)
#         if form.is_valid():
#             city = form.cleaned_data['city']
#             hotels = Hotel.objects.filter(city__icontains=city)
#             return render(request, 'hotels/search_results.html', {'hotels': hotels})
#     else:
#         form = HotelSearchForm()
#     return render(request, 'hotels/search_hotels.html', {'form': form})


# from django.contrib.auth.decorators import login_required
# from django.shortcuts import get_object_or_404, redirect, render
# from .models import Hotel, Booking

# @login_required
# def book_hotel(request, hotel_id):
#     hotel = get_object_or_404(Hotel, id=hotel_id)
#     check_in_date = request.POST['check_in_date']
#     check_out_date = request.POST['check_out_date']
#     Booking.objects.create(user=request.user, hotel=hotel, check_in_date=check_in_date, check_out_date=check_out_date, status='Confirmed')
#     return redirect('payment:success')


# from django.shortcuts import render
# from .models import Hotel

# def search_hotels(request):
#     hotels = Hotel.objects.all()
#     return render(request, 'hotels/search_results.html', {'hotels': hotels})


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Hotel, Booking
from .forms import BookingForm

def search_hotels(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotels/search_results.html', {'hotels': hotels})

@login_required
def book_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.hotel = hotel
            booking.status = 'Confirmed'
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'hotels/book_hotel.html', {'hotel': hotel, 'form': form})

def booking_success(request):
    return render(request, 'hotels/booking_success.html')
