from django.db import models


# Create your models here.
class Destination(models.Model):
    address_label = models.CharField(max_length=200)
    contents = models.TextField(blank=True, default='', null=True)


class Parcel(models.Model):
    label = models.CharField(max_length=200, blank=True, null=True)
    carrier = models.CharField(max_length=100, default="Sea", blank=True, null=True)
    kind = models.CharField(max_length=50, default="Sea", blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, blank=True, null=True)
    items = models.IntegerField(blank=True, null=True)
    contents = models.TextField(blank=True, default='', null=True)
    shipping_cost = models.FloatField(blank=True, null=True)
    date_sent = models.DateField('date sent', blank=True, null=True)
    date_arrived_port = models.DateField('date arrived at port', blank=True, null=True)
    date_sent_port = models.DateField('date sent from port', blank=True, null=True)
    date_arrived_post_office = models.DateField('date arrived at port', blank=True, null=True)
    date_received_destination = models.DateField('date received by destination', blank=True, null=True)
    tracking_us = models.CharField(max_length=50, blank=True, default='', null=True)
    tracking_international = models.CharField(max_length=50, blank=True, default='', null=True)
    delivered = models.BooleanField(default="False", blank=True, null=True)


class Shipping_Update(models.Model):
    parcel = models.ForeignKey(Parcel, on_delete=models.CASCADE, blank=True, null=True)
    update_date = models.CharField(max_length=50, blank=True, default='', null=True)
    update_country = models.CharField(max_length=100, blank=True, default='', null=True)
    update_city = models.CharField(max_length=100, blank=True, default='', null=True)
    update_message_en = models.TextField(blank=True, default='', null=True)
    update_message_details_en = models.TextField(blank=True, default='', null=True)
    update_message_ru = models.TextField(blank=True, default='', null=True)
    update_message_details_ru = models.TextField(blank=True, default='', null=True)
