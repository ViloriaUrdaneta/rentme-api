from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField
    color = models.CharField(max_length=50)
    availabilityStatus = models.BooleanField(default=True)
    mileage = models.IntegerField
    description = models.CharField(max_length=500, null=True, blank=True)
    transmissionType = models.CharField(max_length=50)
    fuelType = models.CharField(max_length=50)
    dailyRate = models.IntegerField
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    
    
class Image(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cars/')

    def __str__(self):
        return f"Image for {self.car.make} {self.car.model}"
    