# Generated by Django 4.1.2 on 2022-12-04 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecomapp", "0006_registercust"),
    ]

    operations = [
        migrations.CreateModel(
            name="get_in_touch",
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
                ("name", models.CharField(max_length=60)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=50)),
                ("message", models.TextField()),
            ],
        ),
    ]
