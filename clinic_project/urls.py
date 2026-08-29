"""
URL configuration for clinic_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from clinic import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("doctors/", views.doctors, name="doctors"),
    path("book-appointment/", views.book_appointment, name="book_appointment"),
    path("appointment-success/", views.appointment_success, name="appointment_success"),
    path("doctor-dashboard/", views.doctor_dashboard, name="doctor_dashboard"),
    path('my-appointments/', views.my_appointments, name='my_appointments'),
 path(
        "book-appointment/",
        views.book_appointment,
        name="book_appointment"
    ),

    path(
        "appointment-success/",
        views.appointment_success,
        name="appointment_success"
    ),

    path(
        "doctor-dashboard/",
        views.doctor_dashboard,
        name="doctor_dashboard"
    ),

    path(
        "accept-appointment/<int:appointment_id>/",
        views.accept_appointment,
        name="accept_appointment"
    ),

    path(
        "reject-appointment/<int:appointment_id>/",
        views.reject_appointment,
        name="reject_appointment"
    ),
   path(
    'add-review/<int:appointment_id>/',
    views.add_review,
    name='add_review'
),
]