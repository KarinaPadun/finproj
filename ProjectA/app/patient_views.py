from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Patient

class PatientListView(ListView):
    model = Patient
    template_name = 'patients/list.html'

class PatientCreateView(CreateView):
    model = Patient
    template_name = 'patients/create.html'
    fields = ['name', 'email', 'phone_number', 'address']

class PatientUpdateView(UpdateView):
    model = Patient
    template_name = 'patients/update.html'
    fields = ['name', 'email', 'phone_number', 'address']

class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'patients/delete.html'
    success_url = '/patients/'
