from django.db import models
from django.contrib.auth.models import AbstractUser

class Patient(models.Model):
    user = models.OneToOneField(AbstractUser, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)

class Doctor(models.Model):
    user = models.OneToOneField(AbstractUser, on_delete=models.CASCADE)
    # Additional doctor-specific fields (e.g., specialty, experience)

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    treatment_plan = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(AbstractUser, on_delete=models.CASCADE, related_name='appointments')
    date_time = models.DateTimeField()
    type = models.CharField(max_length=50, choices=[('TEXT', 'Text Chat'), ('VIDEO', 'Video Call')], default='TEXT')
    notes = models.TextField(blank=True)


