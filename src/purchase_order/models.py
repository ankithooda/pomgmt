from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

from django.db import models

UNIT_CHOICES = [
    ('nos', "Nos")
]

class Vendor(models.Model):
    name = models.CharField(max_length=200)

class PurchaseOrder(models.Model):
    invoice_to = models.ForeignKey(CompanyAddress)
    invoice_contact_person = models.ForeignKey(CompanyPerson)

    ship_to = models.ForeignKey(CompanyAddress)
    ship_contact_person = models.ForeignKey(CompanyPerson)

    vendor = models.ForeignKey(Vendor)

class PurchaseOrderItem(models.Model):
    description = models.CharField(max_length=400)
    hsn_sac = models.CharField(max_length=50)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    unit = models.CharField(max_length=20, choices=UNIT_CHOICES)
    rate = models.IntegerField(validators=[MinValueValidator(1)])
    amount = models.IntegerField(validators=[MinValueValidator(1)])

class CompanyAddress(models.Model):
    key = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=50)
    line1 = models.CharField(max_length=100)
    line2 = models.CharField(max_length=100)
    line3 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    pincode = models.CharField(max_length=20)
    website = models.CharField(max_length=50)

class CompanyPerson(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

