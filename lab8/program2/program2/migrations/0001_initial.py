# Generated by Django 5.2 on 2025-04-10 18:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="workModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("person_name", models.CharField()),
                ("companry_name", models.CharField()),
                ("salary", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="livesModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("street", models.CharField()),
                ("city", models.CharField()),
                (
                    "person_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="program2.workmodel",
                    ),
                ),
            ],
        ),
    ]
