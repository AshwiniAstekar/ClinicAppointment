from django import forms
from .models import Appointment
from .models import Review


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment

        fields = [
            'patient_name',
            'age',
            'occupation',
            'phone',
            'email',
            'appointment_date',
            'appointment_time',
            'symptoms',
            'doctor',
        ]

        widgets = {
            'patient_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }),

            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your age'
            }),
            
           'occupation': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Occupation'
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email'
            }),

            'appointment_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'appointment_time': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time'
            }),

            'symptoms': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe your symptoms',
                'rows': 4
            }),

           'doctor': forms.Select(attrs={
    'class': 'form-control'
}),
        }
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']

        widgets = {
            'rating': forms.Select(
                choices=[
                    (4, '⭐⭐⭐⭐ Excellent'),
                    (3, '⭐⭐⭐ Very Good'),
                    (2, '⭐⭐ Good'),
                    (1, '⭐ Poor'),
                ]
            ),
            'comment': forms.Textarea(attrs={
                'placeholder': 'Write your review...',
                'rows': 5
            }),
        }
        