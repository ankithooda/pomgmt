from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import EmailValidator
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

    # UNIQUE_VENDOR_REFERENCE_NUMBER	Vendor Name	Contact Person	Phone	BANK_ACCOUNT_NUMBER	BANK_IFSC	EMAIL	PHONE2	CONTACT PERSON3

    name                  = models.CharField(max_length=200, unique=True)
    reference_number      = models.CharField(max_length=20, unique=True)
    bank_account_number   = models.CharField(max_length=50, unique=True)
    bank_ifsc_code        = models.CharField(max_length=50)
    gstin                 = models.CharField(max_length=50, unique=True, null=True)

    contact_person_1      = models.CharField(max_length=50)
    email_1               = models.CharField(max_length=50, validators=[EmailValidator])
    phone_1               = models.CharField(max_length=20)

    contact_person_2      = models.CharField(max_length=50, blank=True)
    email_2               = models.CharField(max_length=50, validators=[EmailValidator], blank=True)
    phone_2               = models.CharField(max_length=20, blank=True)

    contact_person_2      = models.CharField(max_length=50, blank=True)
    email_2               = models.CharField(max_length=50, validators=[EmailValidator], blank=True)
    phone_2               = models.CharField(max_length=20, blank=True)


class PurchaseOrder(models.Model):
    voucher_number                = models.CharField(max_length=20)
    purchse_order_date            = models.DateField()
    invoice_to                    = models.ForeignKey(CompanyAddress)
    invoice_contact_person        = models.ForeignKey(CompanyPerson)

    ship_to                       = models.ForeignKey(CompanyAddress)
    ship_contact_person           = models.ForeignKey(CompanyPerson)

    vendor                        = models.ForeignKey(Vendor)

    currency                      = models.CharField(max_length=20, choices=CURRENCY_CHOICES)

    # Additional Charges
    shipping_handling             = models.DecimalField(decimal_places=2, null=True)
    cgst                          = models.DecimalField(decimal_places=2, null=True)
    sgst                          = models.DecimalField(decimal_places=2, null=True)
    igst                          = models.DecimalField(decimal_places=2, null=True)
    discount                      = models.DecimalField(decimal_places=2, null=True)

    ####################### Other Charges ##################################

    other_charges_text_1          = models.CharField(max_length=50, blank=True)
    other_charges_amount_1        = models.DecimalField(null=True)

    other_charges_text_2          = models.CharField(max_length=50, blank=True)
    other_charges_amount_2        = models.DecimalField(null=True)

    other_charges_text_3          = models.CharField(max_length=50, blank=True)
    other_charges_amount_3        = models.DecimalField(null=True)

    other_charges_text_4          = models.CharField(max_length=50, blank=True)
    other_charges_amount_4        = models.DecimalField(null=True)

    other_charges_text_5          = models.CharField(max_length=50, blank=True)
    other_charges_amount_5        = models.DecimalField(null=True)


    # Max Ten Items are supported

    ########################### ITEM 1 #######################################

    description_1       = models.CharField(max_length=400, null=True)
    hsn_sac_1           = models.CharField(max_length=50, blank=True)
    quantity_1          = models.IntegerField(validators=[MinValueValidator(1)], null=True)
    unit_1              = models.CharField(max_length=20, choices=UNIT_CHOICES, null=True)
    rate_1              = models.IntegerField(validators=[MinValueValidator(1)], null=True)
    amount_1            = models.IntegerField(validators=[MinValueValidator(1)], null=True)

    ########################### ITEM 2 #######################################

    description_2       = models.CharField(max_length=400, blank=True)
    hsn_sac_2           = models.CharField(max_length=50, blank=True)
    quantity_2          = models.IntegerField(validators=[MinValueValidator(1)], null=True)
    unit_2              = models.CharField(max_length=20, choices=UNIT_CHOICES, blank=True)
    rate_2              = models.IntegerField(validators=[MinValueValidator(1)], null=True)
    amount_2            = models.IntegerField(validators=[MinValueValidator(1)], null=True)

    ########################### ITEM 3 #######################################

    description_3       = models.CharField(max_length=400, blank=True)
    hsn_sac_3           = models.CharField(max_length=50, blank=True)
    quantity_3          = models.IntegerField(validators=[MinValueValidator(1)], null=True)
    unit_3              = models.CharField(max_length=20, choices=UNIT_CHOICES, blank=True)
    rate_3              = models.IntegerField(validators=[MinValueValidator(1)], null=True)
    amount_3            = models.IntegerField(validators=[MinValueValidator(1)], null=True)

    ########################### ITEM 4 #######################################

    description_4       = models.CharField(max_length=400, blank=True)
    hsn_sac_4           = models.CharField(max_length=50, blank=True)
    quantity_4          = models.IntegerField(validators=[MinValueValidator(1)], null=True)
    unit_4              = models.CharField(max_length=20, choices=UNIT_CHOICES, blank=True)
    rate_4              = models.IntegerField(validators=[MinValueValidator(1)], null=True)
    amount_4            = models.IntegerField(validators=[MinValueValidator(1)], null=True)

    ########################### ITEM 5 #######################################

    description_5       = models.CharField(max_length=400, blank=True)
    hsn_sac_5           = models.CharField(max_length=50, blank=True)
    quantity_5          = models.IntegerField(validators=[MinValueValidator(1)], null=True)
    unit_5              = models.CharField(max_length=20, choices=UNIT_CHOICES, blank=True)
    rate_5              = models.IntegerField(validators=[MinValueValidator(1)], null=True)
    amount_5            = models.IntegerField(validators=[MinValueValidator(1)], null=True)

    ########################### ITEM 6 #######################################

    description_6       = models.CharField(max_length=400)
    hsn_sac_6           = models.CharField(max_length=50)
    quantity_6          = models.IntegerField(validators=[MinValueValidator(1)], null=True)
    unit_6              = models.CharField(max_length=20, choices=UNIT_CHOICES)
    rate_6              = models.IntegerField(validators=[MinValueValidator(1)], null=True)
    amount_6            = models.IntegerField(validators=[MinValueValidator(1)], null=True)


    ########################### ITEM 7 #######################################

    description_7       = models.CharField(max_length=400, blank=True)
    hsn_sac_7           = models.CharField(max_length=50, blank=True)
    quantity_7          = models.IntegerField(validators=[MinValueValidator(1)], null=True)
    unit_7              = models.CharField(max_length=20, choices=UNIT_CHOICES, blank=True)
    rate_7              = models.IntegerField(validators=[MinValueValidator(1)], null=True)
    amount_7            = models.IntegerField(validators=[MinValueValidator(1)], null=True)

    ########################### ITEM 8 #######################################

    description_8       = models.CharField(max_length=400, blank=True)
    hsn_sac_8           = models.CharField(max_length=50, blank=True)
    quantity_8          = models.IntegerField(validators=[MinValueValidator(1)], null=True)
    unit_8              = models.CharField(max_length=20, choices=UNIT_CHOICES, blank=True)
    rate_8              = models.IntegerField(validators=[MinValueValidator(1)], null=True)
    amount_8            = models.IntegerField(validators=[MinValueValidator(1)], null=True)

    ########################### ITEM 9 #######################################

    description_9       = models.CharField(max_length=400, blank=True)
    hsn_sac_9           = models.CharField(max_length=50, blank=True)
    quantity_9          = models.IntegerField(validators=[MinValueValidator(1)], null=True)
    unit_9              = models.CharField(max_length=20, choices=UNIT_CHOICES, blank=True)
    rate_9              = models.IntegerField(validators=[MinValueValidator(1)], null=True)
    amount_9            = models.IntegerField(validators=[MinValueValidator(1)], null=True)

    ########################### ITEM 10 #######################################

    description_10       = models.CharField(max_length=400, blank=True)
    hsn_sac_10           = models.CharField(max_length=50, blank=True)
    quantity_10          = models.IntegerField(validators=[MinValueValidator(1)], null=True)
    unit_10              = models.CharField(max_length=20, choices=UNIT_CHOICES, blank=True)
    rate_10              = models.IntegerField(validators=[MinValueValidator(1)], null=True)
    amount_10            = models.IntegerField(validators=[MinValueValidator(1)], null=True)

class CompanyAddress(models.Model):
    key           = models.CharField(max_length=20, unique=True)
    name          = models.CharField(max_length=50)
    line1         = models.CharField(max_length=100)
    line2         = models.CharField(max_length=100)
    line3         = models.CharField(max_length=100)
    city          = models.CharField(max_length=50)
    state         = models.CharField(max_length=50)
    country       = models.CharField(max_length=50)
    pincode       = models.CharField(max_length=20)
    website       = models.CharField(max_length=50)
    gstin         = models.CharField(max_length=50)

class CompanyPerson(models.Model):
    name          = models.CharField(max_length=50)
    phone         = models.CharField(max_length=50)
    email         = models.CharField(max_length=50)

