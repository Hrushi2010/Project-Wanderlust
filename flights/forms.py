from django import forms
from .models import Airport

class FlightSearchForm(forms.Form):
    departure_airport = forms.ModelChoiceField(queryset=Airport.objects.all())
    arrival_airport = forms.ModelChoiceField(queryset=Airport.objects.all())
    departure_date = forms.DateField(widget=forms.SelectDateWidget)
