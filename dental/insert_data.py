from .models import Patient
from random import choice

# Define a list of doctor_ids (1 and 2 in this case)
assigned_doctor_id = [1, 2]

# Get all existing Patient records
patients = Patient.objects.all()

# Update the assigned_doctor_id field for each patient randomly
for patient in patients:
    patient.assigned_doctor_id = choice(assigned_doctor_id)
    patient.save()
