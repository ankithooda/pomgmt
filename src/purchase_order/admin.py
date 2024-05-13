from django.contrib import admin

from .models import Vendor, PurchaseOrderItem, CompanyAddress, CompanyPerson
admin.site.register(Vendor)
admin.site.register(PurchaseOrderItem)
admin.site.register(CompanyAddress)
admin.site.register(CompanyPerson)
