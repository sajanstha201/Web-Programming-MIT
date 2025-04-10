# Generated by Django 5.2 on 2025-04-10 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DIR",
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
                ("url", models.CharField()),
                ("num_visited", models.IntegerField()),
                ("num_like", models.IntegerField()),
            ],
        ),
    ]
