from celery import shared_task

@shared_task
def send_appointment_reminder(patient_id, appointment_time):
    pass

@shared_task
def process_lab_results(patient_id, lab_data):
    pass
