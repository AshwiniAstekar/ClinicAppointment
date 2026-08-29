from django.db import models




class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    email = models.EmailField(default="")

    def __str__(self):
        return self.name

class Appointment(models.Model):

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Accepted", "Accepted"),
        ("Rejected", "Rejected"),
    ]

    
    patient_name = models.CharField(max_length=100)
    age = models.IntegerField()
    occupation = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    symptoms = models.TextField()
    
   
    doctor = models.ForeignKey(
        
        Doctor,
        on_delete=models.CASCADE
    )
    status = models.CharField(
            max_length=20,
            choices=STATUS_CHOICES,
            default='Pending'
        )
     

    created_at = models.DateTimeField(auto_now_add=True)



   
    def __str__(self):
        return self.patient_name



class Review(models.Model):
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    patient_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    rating = models.IntegerField(default=5)

    comment = models.TextField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.doctor:
            return f"{self.patient_name} - {self.doctor.name}"
        return f"{self.patient_name} - No doctor"