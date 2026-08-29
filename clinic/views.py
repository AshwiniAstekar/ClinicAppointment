# from django.shortcuts import render, redirect
# from .models import Doctor, Appointment
# from .forms import AppointmentForm


# # Home Page
# def home(request):
#     return render(request, "clinic/home.html")


# # About Page
# def about(request):
#     return render(request, "clinic/about.html")
# def book_appointment(request):

#     return render(request, "clinic/book_appointment.html")


# # Doctors Page
# def doctors(request):
#     doctors_list = Doctor.objects.all()

#     return render(request, "clinic/doctors.html", {
#         "doctors": doctors_list
#     })


# # Book Appointment
# def book_appointment(request):

#     if request.method == "POST":
#         form = AppointmentForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return redirect("appointment_success")

#     else:
#         form = AppointmentForm()

#     return render(request, "clinic/book_appointment.html", {
#         "form": form
#     })


# # Appointment Success Page
# def appointment_success(request):
#     return render(request, "clinic/appointment_success.html")


# # Doctor Dashboard
# def doctor_dashboard(request):
#     appointments = Appointment.objects.all().order_by(
#         "-appointment_date"
#     )

#     return render(request, "clinic/doctor_dashboard.html", {
#         "appointments": appointments
#     })

from django.shortcuts import  get_object_or_404, render, redirect
from .models import Doctor, Appointment, Review
from .forms import AppointmentForm
from .forms import ReviewForm




# Home Page
def home(request):
    return render(request, "clinic/home.html")


# About Page
def about(request):
    return render(request, "clinic/about.html")


# Doctors Page
def doctors(request):
    doctors_list = Doctor.objects.all()

    return render(request, "clinic/doctors.html", {
        "doctors": doctors_list
    })


# Book Appointment
def book_appointment(request):

    if request.method == "POST":
        form = AppointmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("appointment_success")

    else:
        form = AppointmentForm()

    return render(request, "clinic/book_appointment.html", {
        "form": form
    })


# Appointment Success Page
def appointment_success(request):
    return render(request, "clinic/appointment_success.html")


# Doctor Dashboard
def doctor_dashboard(request):
    appointments = Appointment.objects.all().order_by(
        "-appointment_date",
        "-appointment_time"
    )

    reviews = Review.objects.all().order_by("-created_at")

    return render(
        request,
        "clinic/doctor_dashboard.html",
        {
            "appointments": appointments,
            "reviews": reviews,
        }
    )


# Accept Appointment
def accept_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    appointment.status = "Accepted"
    appointment.save()

    return redirect("doctor_dashboard")


# Reject Appointment
def reject_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    appointment.status = "Rejected"
    appointment.save()

    return redirect("doctor_dashboard")


def my_appointments(request):
    email = request.GET.get('email')

    appointments = Appointment.objects.filter(
        email=email
    )

    reviews = Review.objects.filter(
        patient_name__in=appointments.values_list(
            'patient_name',
            flat=True
        )
    )

    return render(
        request,
        'clinic/my_appointments.html',
        {
            'appointments': appointments,
            'reviews': reviews
        }
    )

def add_review(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)

            review.doctor = appointment.doctor
            review.patient_name = appointment.patient_name

            review.save()

           

            return redirect('doctor_dashboard')
    else:
        form = ReviewForm()

    return render(request, 'clinic/add_review.html', {
        'form': form,
        'appointment': appointment
    })