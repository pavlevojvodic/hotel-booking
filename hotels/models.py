from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class PropertyType(models.Model):
    name = models.CharField(max_length=60)
    icon_url = models.CharField(max_length=500, blank=True, null=True)
    parent_category = models.ForeignKey('self', blank=True, null=True, related_name='subcategories', on_delete=models.CASCADE)
    def __str__(self): return self.name

class Location(models.Model):
    name = models.CharField(max_length=60)
    parent_category = models.ForeignKey('self', blank=True, null=True, related_name='sublocations', on_delete=models.CASCADE)
    type = models.CharField(max_length=60, blank=True, null=True)
    def __str__(self): return self.name

class HotelProperty(models.Model):
    class Currency(models.TextChoices):
        USD = ("USD", _("US Dollar"))
        EUR = ("EUR", _("Euro"))
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    type = models.ForeignKey(PropertyType, on_delete=models.CASCADE, blank=True, null=True, related_name="properties")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True, related_name="properties")
    images = models.JSONField(default=list, blank=True)
    lowest_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    highest_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    lat = models.DecimalField(max_digits=20, decimal_places=17)
    long = models.DecimalField(max_digits=20, decimal_places=17)
    currency = models.CharField(max_length=3, choices=Currency.choices, default=Currency.EUR)
    description_eng = models.TextField(blank=True, null=True)
    description_srb = models.TextField(blank=True, null=True)
    description_ger = models.TextField(blank=True, null=True)
    rooms_number = models.CharField(max_length=5, blank=True, null=True)
    features_eng = models.CharField(max_length=200, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self): return f"{self.title} - {self.subtitle}"

class Reservation(models.Model):
    property = models.ForeignKey(HotelProperty, on_delete=models.CASCADE, related_name="reservations")
    user_name = models.CharField(max_length=255)
    user_email = models.CharField(max_length=255)
    user_phone = models.CharField(max_length=255, blank=True, null=True)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    def __str__(self): return f"{self.property.title} - {self.user_name}"

class Newsletter(models.Model):
    email = models.CharField(max_length=255)
    def __str__(self): return self.email

class CustomerMessage(models.Model):
    ts = models.DateTimeField(default=timezone.now)
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.CharField(max_length=2000, blank=True, null=True)
    def __str__(self): return f"{self.customer_name} - {self.subject}"
