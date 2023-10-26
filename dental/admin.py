# admin.py
from django.contrib import admin
from import_export.admin import ExportActionMixin
from .models import Doctor, Patient, PatientPayment, MyExpenses
from dental.resources import PatientPaymentResource


class DoctorAdmin(ExportActionMixin, admin.ModelAdmin):
    list_filter = ("name",)
    search_fields = ("name",)
    list_per_page = 5  # No of records per page


class PatientAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ("name", "gender", "age", "assigned_doctor", "contact_number")
    search_fields = ("name",)
    list_filter = ("gender", "age", "assigned_doctor")
    list_per_page = 30


class PatientPaymentAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = PatientPaymentResource
    list_display = (
        "get_patient_name",
        "payment_date",
        "description",
        "amount",
        "payment_to_account",
    )
    search_fields = (
        "patient__name",
        "payment_date",
        "description",
        "amount",
        "payment_to_account",
    )
    list_filter = ("patient", "payment_date", "payment_to_account")
    list_per_page = 50


class MyExpensesAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ("expense_name", "paid_amount", "expense_date", "expense_details")
    search_fields = ("expense_name", "paid_amount", "expense_date")
    list_filter = ("expense_name", "paid_amount", "expense_date")
    list_per_page = 30


# Register the models with custom admin configurations
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(PatientPayment, PatientPaymentAdmin)
admin.site.register(MyExpenses, MyExpensesAdmin)
