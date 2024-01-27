# Generated by Django 5.0 on 2024-01-27 21:11

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ContactUs",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_updated", models.DateTimeField(auto_now=True)),
                ("email", models.EmailField(db_index=True, max_length=254)),
                ("full_name", models.CharField(max_length=255)),
                ("message", models.TextField()),
                ("enquiry_type", models.CharField(max_length=255)),
                ("subject", models.CharField(max_length=255)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
