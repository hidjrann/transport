import datetime
from django import forms
from django.core.exceptions import ValidationError
from main import models

# Tarix üçün HTML5 date input istifadə edirik
class DateInput(forms.DateInput):
    input_type = 'date'

class BookForm(forms.ModelForm):
    class Meta:
        model = models.Booking
        fields = ('car', 'booking_start_date', 'booking_end_date',)
        widgets = {
            'booking_start_date': DateInput(),
            'booking_end_date': DateInput()
        }

    def clean_booking_start_date(self):
        data = self.cleaned_data.get('booking_start_date')
        if data and data < datetime.date.today():
            raise ValidationError('Başlama tarixi keçmişdə ola bilməz.')
        return data

    def clean_booking_end_date(self):
        data = self.cleaned_data.get('booking_end_date')
        if data and data < datetime.date.today():
            raise ValidationError('Bitmə tarixi keçmişdə ola bilməz.')
        return data

# Ride üçün form
class RideForm(forms.ModelForm):
    class Meta:
        model = models.Ride
        fields = ('origin', 'destination',)
