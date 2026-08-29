from django.contrib import admin
from .models import Doctor, Appointment
from django.contrib import admin
from .models import Review

admin.site.register(Review)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'specialization',
    )


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'patient_name',
        'age',
        'phone',
        'doctor',
        'appointment_date',
        'appointment_time',
    )

    list_filter = (
        'doctor',
        'appointment_date',
    )