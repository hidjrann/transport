from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='car_images')
    description = models.TextField()
    daily_rent = models.IntegerField(default=0)
    is_available = models.BooleanField()

    def get_absolute_url(self):
        return reverse('car-details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Booking(models.Model):
    customer_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )
    car = models.ForeignKey(Car, blank=True, null=True, on_delete=models.CASCADE,)
    booking_start_date = models.DateField()
    booking_end_date = models.DateField()
    is_approved = models.BooleanField(default=False)

    @property
    def date_def(self):
        day =  int((self.booking_end_date - self.booking_start_date).days)
        return day

    @property
    def cost(self):
        day = int((self.booking_end_date - self.booking_start_date).days)
        
        if self.car.daily_rent is not None:
            cost = int(self.car.daily_rent)
        else:
            cost = 0
        return (cost*day)

class Ride(models.Model):
    customer_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    distance = models.FloatField(max_length=30, default=6.2)
    cost = models.FloatField(max_length=30, default=250.0)
    approved = models.BooleanField(default=False)