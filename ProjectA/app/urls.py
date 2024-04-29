from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, MedicalRecordViewSet

router = DefaultRouter()
router.register('patients', PatientViewSet)
router.register('medical-records', MedicalRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
