from rest_framework import serializers
from .models import Patient, MedicalRecord, Appointment

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'user', 'name', 'email', 'phone_number', 'date_of_birth']

class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = ['id', 'patient', 'diagnosis', 'treatment_plan', 'created_at']

class AppointmentSerializer(serializers.ModelSerializer):
    doctor_username = serializers.CharField(source='doctor.username', read_only=True)  # Show doctor username instead of ID

    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'doctor_username', 'date_time', 'type', 'notes']



