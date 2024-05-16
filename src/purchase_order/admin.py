from django.contrib import admin

from .models import Vendor, PurchaseOrder, CompanyAddress, CompanyPerson

class VendorAdmin(admin.ModelAdmin):
    list_display = ["name", "reference_number"]
    readonly_fields = ["reference_number"]

    fieldsets = [
        (
            None,
            {
                "fields": [
                    "reference_number",
                    "name",
                    "bank_account_number",
                    "bank_ifsc_code",
                    "gstin",
                    "contact_person_1",
                    "email_1",
                    "phone_1"
                ],
            },
        ),
        (
            "Additional Contact Persons Info",
            {
                "classes":["collapse"],
                "fields": [
                    "contact_person_2",
                    "email_2",
                    "phone_2",
                    "contact_person_3",
                    "email_3",
                    "phone_3"
                ],
            },
        ),
    ]


class CompanyAddressAdmin(admin.ModelAdmin):
    list_display = ["key", "name"]


class CompanyPersonAdmin(admin.ModelAdmin):
    list_display = ["name"]


class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ["voucher_number", "purchse_order_date", "vendor"]
    readonly_fields = [
        "voucher_number",
        "total",
        "amount_1", "amount_2", "amount_3", "amount_4", "amount_5",
        "amount_6", "amount_7", "amount_8", "amount_9", "amount_10"
    ]
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "voucher_number",
                    "vendor",
                    "purchse_order_date",
                    "invoice_to",
                    "invoice_contact_person",
                    "ship_to",
                    "ship_contact_person",
                    "currency",
                    "total"
                ],
            },
        ),
        (
            "Line Item 1",
            {
                "classes":["collapse"],
                "fields": [
                    "description_1", "hsn_sac_1",
                    "quantity_1", "unit_1",
                    "rate_1", "amount_1"
                ]
            }
        ),
        (
            "Line Item 2",
            {
                "classes":["collapse"],
                "fields": [
                    "description_2", "hsn_sac_2",
                    "quantity_2", "unit_2",
                    "rate_2", "amount_2"
                ]
            }
        ),
        (
            "Line Item 3",
            {
                "classes":["collapse"],
                "fields": [
                    "description_3", "hsn_sac_3",
                    "quantity_3", "unit_3",
                    "rate_3", "amount_3"
                ]
            }
        ),
        (
            "Line Item 4",
            {
                "classes":["collapse"],
                "fields": [
                    "description_4", "hsn_sac_4",
                    "quantity_4", "unit_4",
                    "rate_4", "amount_4"
                ]
            }
        ),
        (
            "Line Item 5",
            {
                "classes":["collapse"],
                "fields": [
                    "description_5", "hsn_sac_5",
                    "quantity_5", "unit_5",
                    "rate_5", "amount_5"
                ]
            }
        ),
        (
            "Line Item 6",
            {
                "classes":["collapse"],
                "fields": [
                    "description_6", "hsn_sac_6",
                    "quantity_6", "unit_6",
                    "rate_6", "amount_6"
                ]
            }
        ),
        (
            "Line Item 7",
            {
                "classes":["collapse"],
                "fields": [
                    "description_7", "hsn_sac_7",
                    "quantity_7", "unit_7",
                    "rate_7", "amount_7"
                ]
            }
        ),
        (
            "Line Item 8",
            {
                "classes":["collapse"],
                "fields": [
                    "description_8", "hsn_sac_8",
                    "quantity_8", "unit_8",
                    "rate_8", "amount_8"
                ]
            }
        ),
        (
            "Line Item 9",
            {
                "classes":["collapse"],
                "fields": [
                    "description_9", "hsn_sac_9",
                    "quantity_9", "unit_9",
                    "rate_9", "amount_9"
                ]
            }
        ),
        (
            "Line Item 10",
            {
                "classes":["collapse"],
                "fields": [
                    "description_10", "hsn_sac_10",
                    "quantity_10", "unit_10",
                    "rate_10", "amount_10"
                ]
            }
        ),
        (
            "Additional Charges & Discount",
            {
                "classes": ["collapse"],
                "fields": ["shipping_handling", "cgst", "sgst", "igst", "discount"],
            },
        ),
        (
            "Custom Charges",
            {
                "classes":["collapse"],
                "fields": [
                    ("other_charges_text_1", "other_charges_amount_1"),
                    ("other_charges_text_2", "other_charges_amount_2"),
                    ("other_charges_text_3", "other_charges_amount_3")
                ]
            }
        ),
    ]


admin.site.register(Vendor, VendorAdmin)
admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
admin.site.register(CompanyAddress)
admin.site.register(CompanyPerson)

