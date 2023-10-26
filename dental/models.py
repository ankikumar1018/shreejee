# models.py
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from dental.choices import PaymentChoices, Gender, GovernmentID


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="doctor_photos/", null=True, blank=True)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=100)
    patient_photo = models.ImageField(
        upload_to="Patient_photos/", null=True, blank=True
    )
    gender = models.CharField(max_length=1, choices=Gender.GENDER_CHOICES)
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(120)])
    contact_number = models.CharField(max_length=15, unique=True)
    assigned_doctor = models.ForeignKey(
        Doctor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_patients",
    )
    issue_description = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    government_id_type = models.CharField(
        max_length=20, choices=GovernmentID.GOVERNMENT_ID_CHOICES, null=True, blank=True
    )
    government_id_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name


class PatientPayment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    payment_date = models.DateField(auto_now_add=True, blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_to_account = models.CharField(
        max_length=50,
        choices=PaymentChoices.PAYMENT_CHOICES,
        default="Account Not Selected",
    )
    patient_bill_image = models.ImageField(
        upload_to="PatientPayment_photos/", null=True, blank=True
    )
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Patient Payment"

    def get_patient_name(self):
        return self.patient.name

    get_patient_name.short_description = (
        "Patient Name"  # Sets column name in admin interface
    )

    def __str__(self):
        return f"Expense for {self.patient.name} - {self.payment_date}"


class MyExpenses(models.Model):
    expense_name = models.CharField(max_length=300, verbose_name="Expense Name")
    paid_amount = models.CharField(max_length=100)
    expense_date = models.DateField(auto_now_add=True, blank=False)
    expense_bill_image = models.ImageField(
        upload_to="MyExpenses_photos/", null=True, blank=True
    )
    expense_details = models.TextField(
        null=True, default="Details not provided", verbose_name="Expense Details"
    )

    class Meta:
        verbose_name = "My Expense"

    def __str__(self):
        return self.expense_name
