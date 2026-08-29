from django.db import migrations


def create_default_doctors(apps, schema_editor):
    Doctor = apps.get_model("clinic", "Doctor")

    Doctor.objects.get_or_create(
        name="Dr. Tejashree N Patil",
        defaults={
            "specialization": "General Physician",
            "email": "tejashreep@gmail.com",
        },
    )

    Doctor.objects.get_or_create(
        name="Dr. Mayur Mohan Astekar",
        defaults={
            "specialization": "General Physician",
            "email": "mayur@gmail.com",
        },
    )


class Migration(migrations.Migration):

    dependencies = [
        ("clinic", "0005_remove_review_appointment_review_doctor_and_more"),
    ]

    operations = [
        migrations.RunPython(create_default_doctors),
    ]