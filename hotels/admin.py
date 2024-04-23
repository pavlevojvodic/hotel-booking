from django.contrib import admin
from .models import PropertyType, Location, HotelProperty, Reservation, Newsletter, CustomerMessage
for m in [PropertyType, Location, HotelProperty, Reservation, Newsletter, CustomerMessage]:
    admin.site.register(m)
