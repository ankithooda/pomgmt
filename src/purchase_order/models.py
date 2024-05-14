from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

from django.db import models

UNIT_CHOICES = [
    ('nos', "Nos")
]

CURRENCY_CHOICES = [
    ('USD', '$')
    ('INR', 'Rs.')
]

class Vendor(models.Model):
    name = models.CharField(max_length=200)

class PurchaseOrder(models.Model):
    invoice_to = models.ForeignKey(CompanyAddress)
    invoice_contact_person = models.ForeignKey(CompanyPerson)

    ship_to = models.ForeignKey(CompanyAddress)
    ship_contact_person = models.ForeignKey(CompanyPerson)

    vendor = models.ForeignKey(Vendor)

    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES)
    # Shipping and Handling
    # CGST
    # SGST
    # IGST
    # Others(with text box)
    # Discount
    
    # Max Ten Items are supported

    ########################### ITEM 1 #######################################

    description_1       = models.CharField(max_length=400)
    hsn_sac_1           = models.CharField(max_length=50)
    quantity_1          = models.IntegerField(validators=[MinValueValidator(1)])
    unit_1              = models.CharField(max_length=20, choices=UNIT_CHOICES)
    rate_1             = models.IntegerField(validators=[MinValueValidator(1)])
    amount_1            = models.IntegerField(validators=[MinValueValidator(1)])

    ########################### ITEM 2 #######################################

    description_2       = models.CharField(max_length=400)
    hsn_sac_2           = models.CharField(max_length=50)
    quantity_2          = models.IntegerField(validators=[MinValueValidator(1)])
    unit_2              = models.CharField(max_length=20, choices=UNIT_CHOICES)
    rate_2              = models.IntegerField(validators=[MinValueValidator(1)])
    amount_2            = models.IntegerField(validators=[MinValueValidator(1)])

    ########################### ITEM 3 #######################################

    description_3       = models.CharField(max_length=400)
    hsn_sac_3           = models.CharField(max_length=50)
    quantity_3          = models.IntegerField(validators=[MinValueValidator(1)])
    unit_3              = models.CharField(max_length=20, choices=UNIT_CHOICES)
    rate_3              = models.IntegerField(validators=[MinValueValidator(1)])
    amount_3            = models.IntegerField(validators=[MinValueValidator(1)])

    ########################### ITEM 4 #######################################

    description_4       = models.CharField(max_length=400)
    hsn_sac_4           = models.CharField(max_length=50)
    quantity_4          = models.IntegerField(validators=[MinValueValidator(1)])
    unit_4              = models.CharField(max_length=20, choices=UNIT_CHOICES)
    rate_4              = models.IntegerField(validators=[MinValueValidator(1)])
    amount_4            = models.IntegerField(validators=[MinValueValidator(1)])

    ########################### ITEM 5 #######################################

    description_5       = models.CharField(max_length=400)
    hsn_sac_5           = models.CharField(max_length=50)
    quantity_5          = models.IntegerField(validators=[MinValueValidator(1)])
    unit_5              = models.CharField(max_length=20, choices=UNIT_CHOICES)
    rate_5              = models.IntegerField(validators=[MinValueValidator(1)])
    amount_5            = models.IntegerField(validators=[MinValueValidator(1)])

    ########################### ITEM 6 #######################################

    description_6       = models.CharField(max_length=400)
    hsn_sac_6           = models.CharField(max_length=50)
    quantity_6          = models.IntegerField(validators=[MinValueValidator(1)])
    unit_6              = models.CharField(max_length=20, choices=UNIT_CHOICES)
    rate_6              = models.IntegerField(validators=[MinValueValidator(1)])
    amount_6            = models.IntegerField(validators=[MinValueValidator(1)])


    ########################### ITEM 7 #######################################

    description_7       = models.CharField(max_length=400)
    hsn_sac_7           = models.CharField(max_length=50)
    quantity_7          = models.IntegerField(validators=[MinValueValidator(1)])
    unit_7              = models.CharField(max_length=20, choices=UNIT_CHOICES)
    rate_7              = models.IntegerField(validators=[MinValueValidator(1)])
    amount_7            = models.IntegerField(validators=[MinValueValidator(1)])

    ########################### ITEM 8 #######################################

    description_8       = models.CharField(max_length=400)
    hsn_sac_8           = models.CharField(max_length=50)
    quantity_8          = models.IntegerField(validators=[MinValueValidator(1)])
    unit_8              = models.CharField(max_length=20, choices=UNIT_CHOICES)
    rate_8              = models.IntegerField(validators=[MinValueValidator(1)])
    amount_8            = models.IntegerField(validators=[MinValueValidator(1)])

    ########################### ITEM 9 #######################################

    description_9       = models.CharField(max_length=400)
    hsn_sac_9           = models.CharField(max_length=50)
    quantity_9          = models.IntegerField(validators=[MinValueValidator(1)])
    unit_9              = models.CharField(max_length=20, choices=UNIT_CHOICES)
    rate_9              = models.IntegerField(validators=[MinValueValidator(1)])
    amount_9            = models.IntegerField(validators=[MinValueValidator(1)])

    ########################### ITEM 10 #######################################

    description_10       = models.CharField(max_length=400)
    hsn_sac_10           = models.CharField(max_length=50)
    quantity_10          = models.IntegerField(validators=[MinValueValidator(1)])
    unit_10              = models.CharField(max_length=20, choices=UNIT_CHOICES)
    rate_10              = models.IntegerField(validators=[MinValueValidator(1)])
    amount_10            = models.IntegerField(validators=[MinValueValidator(1)])


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

