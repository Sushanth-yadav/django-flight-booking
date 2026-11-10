from django.contrib import admin
from .models import Available, Booking

# Register your models here.
@admin.register(Available)
class AvailableAdmin(admin.ModelAdmin):
    list_display = ('flightno', 'comp', 'flightn', 'fromm', 'to', 'departure', 'date', 'price')
    search_fields = ('flightno', 'comp', 'flightn', 'fromm', 'to')
    list_filter = ('comp', 'fromm', 'to', 'date')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('flightno', 'name', 'seat', 'seatno', 'fromm', 'to', 'date', 'price')
    search_fields = ('name', 'flightno', 'aadhar', 'email', 'pnum')
    list_filter = ('seat', 'comp', 'date')
