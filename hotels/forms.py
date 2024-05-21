from django import forms

class HotelSearchForm(forms.Form):
    city = forms.CharField(max_length=100)
    check_in_date = forms.DateField(widget=forms.SelectDateWidget)
    check_out_date = forms.DateField(widget=forms.SelectDateWidget)


from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in_date', 'check_out_date']
        widgets = {
            'check_in_date': forms.DateInput(attrs={'type': 'date'}),
            'check_out_date': forms.DateInput(attrs={'type': 'date'}),
        }
