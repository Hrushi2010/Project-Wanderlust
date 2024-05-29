# from django import forms
# from .models import Airport

# class FlightSearchForm(forms.Form):
#     departure_airport = forms.ModelChoiceField(queryset=Airport.objects.all())
#     arrival_airport = forms.ModelChoiceField(queryset=Airport.objects.all())
#     departure_date = forms.DateField(widget=forms.SelectDateWidget)


# from django import forms
# from .models import Airport

# class FlightSearchForm(forms.Form):
#     departure_airport = forms.ModelChoiceField(queryset=Airport.objects.all())
#     arrival_airport = forms.ModelChoiceField(queryset=Airport.objects.all())
#     departure_date = forms.DateField(widget=forms.SelectDateWidget)


# flights/forms.py

from django import forms
from .models import Flight, Booking, Airport

class SearchForm(forms.Form):
    departure_airport = forms.ModelChoiceField(queryset=Airport.objects.all(), label="Departure Airport")
    arrival_airport = forms.ModelChoiceField(queryset=Airport.objects.all(), label="Arrival Airport")
    departure_date = forms.DateField(widget=forms.SelectDateWidget, label="Departure Date")

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['passenger_name', 'amount']
