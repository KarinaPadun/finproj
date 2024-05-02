from django.db import models
from django.contrib.auth.models import AbstractUser

class PatientProfile(models.Model):
    user = models.OneToOneField(AbstractUser, on_delete=models.CASCADE)
    # Additional patient-specific fields (e.g., date_of_birth, medical_history)

class DoctorProfile(models.Model):
    user = models.OneToOneField(AbstractUser, on_delete=models.CASCADE)
    # Additional doctor-specific fields (e.g., specialty, experience)
