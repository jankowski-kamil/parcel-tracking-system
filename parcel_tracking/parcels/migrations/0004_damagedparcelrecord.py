# Generated by Django 5.0.8 on 2024-08-29 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("parcels", "0003_parcel_recipient_alter_parcel_courier"),
    ]

    operations = [
        migrations.CreateModel(
            name="DamagedParcelRecord",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("package_id", models.TextField(max_length=255)),
            ],
        ),
    ]
