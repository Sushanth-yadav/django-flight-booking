from django.db import models

# Create your models here.
class Available(models.Model):
    comp=models.CharField(max_length=20)
    flightn=models.CharField(max_length=20)
    flightno=models.CharField()
    fromm=models.CharField(max_length=20)
    to=models.CharField(max_length=20)
    departure=models.CharField(max_length=20)
    date=models.CharField(max_length=15)
    price=models.IntegerField()

class Booking(models.Model):
    comp=models.CharField(max_length=20)
    flightn=models.CharField(max_length=20)
    flightno=models.CharField()
    fromm=models.CharField(max_length=20)
    to=models.CharField(max_length=20)
    departure=models.CharField(max_length=20)
    date=models.CharField(max_length=15)
    price=models.IntegerField()
    name=models.CharField(max_length=20)
    aadhar=models.IntegerField()
    email=models.EmailField(blank=True)
    age=models.IntegerField()
    seat=models.CharField(max_length=10)
    seatno=models.IntegerField()
    pnum=models.IntegerField(blank=True)