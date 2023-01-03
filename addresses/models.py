from django.db import models


class Address(models.Model):
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    number = models.CharField(max_length=4)
    zipcode = models.CharField(max_length=11)
