#from django.urls import path
#from . import views

#urlpatterns = [
 #   path('', views.home, name='home'),
  #  path('book-appointment/', views.book_appointment, name='book_appointment'),
#]
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('book-appointment/', views.book_appointment, name='book_appointment'),
#     path('appointment-success/', views.appointment_success, name='appointment_success'),
#     path('doctor-dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
# ]
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('book-appointment/', views.book_appointment, name='book_appointment'),
#     path('appointment-success/', views.appointment_success, name='appointment_success'),
#     path('doctor-dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
# ]
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),

#     path('about/', views.about, name='about'),

#     path('doctors/', views.doctors, name='doctors'),

#     path('book-appointment/', views.book_appointment, name='book_appointment'),

#     path('appointment-success/', views.appointment_success, name='appointment_success'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('doctors/', views.doctors, name='doctors'),
    path("book-appointment/", views.book_appointment, name="book_appointment"),
    path("appointment-success/", views.appointment_success, name="appointment_success"),

path(
        'my-appointments/',
        views.my_appointments,
        name='my_appointments'
    ),
    
path(
    "add-review/<int:appointment_id>/",
    views.add_review,
    name="add_review"
),

]


