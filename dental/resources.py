from import_export import resources, fields
from .models import PatientPayment


class PatientPaymentResource(resources.ModelResource):
    patient_name = fields.Field(attribute="patient__name", column_name="Patient Name")

    class Meta:
        model = PatientPayment
        fields = (
            "id",
            "patient_name",
            "payment_date",
            "description",
            "amount",
            "payment_to_account",
        )
