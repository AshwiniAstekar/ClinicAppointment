from django.db import migrations


def add_mayur_doctor(apps, schema_editor):
    Doctor = apps.get_model("clinic", "Doctor")

    Doctor.objects.get_or_create(
        name="Dr. Mayur Mohan Astekar",
        defaults={
            "specialization": "General Physician",
            "email": "mayur@gmail.com",
        },
    )


class Migration(migrations.Migration):

    dependencies = [
        ("clinic", "0006_add_default_doctor"),
    ]

    operations = [
        migrations.RunPython(add_mayur_doctor),
    ]