from .celery import app
from .models import Appointment

def schedule_appointment(patient_id, doctor_id, date_time):
  appointment = Appointment.objects.create(patient_id=patient_id, doctor_id=doctor_id, date_time=date_time)
  send_appointment_reminder.delay(patient_id, date_time)
  return appointment
