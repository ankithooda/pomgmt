from django.contrib import admin

from .models import Vendor, PurchaseOrder, CompanyAddress, CompanyPerson
admin.site.register(Vendor)
admin.site.register(PurchaseOrder)
admin.site.register(CompanyAddress)
admin.site.register(CompanyPerson)
