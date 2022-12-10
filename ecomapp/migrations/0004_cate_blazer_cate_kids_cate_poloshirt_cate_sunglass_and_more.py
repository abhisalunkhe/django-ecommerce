# Generated by Django 4.1.2 on 2022-11-30 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecomapp", "0003_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="cate_blazer",
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
                ("name", models.CharField(max_length=25)),
                ("price", models.IntegerField()),
                ("image", models.ImageField(upload_to="cate_blazer")),
                ("visible", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="cate_kids",
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
                ("name", models.CharField(max_length=25)),
                ("price", models.IntegerField()),
                ("image", models.ImageField(upload_to="cate_kids")),
                ("visible", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="cate_poloshirt",
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
                ("name", models.CharField(max_length=25)),
                ("price", models.IntegerField()),
                ("image", models.ImageField(upload_to="cate_poloshirt")),
                ("visible", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="cate_sunglass",
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
                ("name", models.CharField(max_length=25)),
                ("price", models.IntegerField()),
                ("image", models.ImageField(upload_to="cate_sunglass")),
                ("visible", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="cate_tshirt",
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
                ("name", models.CharField(max_length=25)),
                ("price", models.IntegerField()),
                ("image", models.ImageField(upload_to="cate_tshirt")),
                ("visible", models.BooleanField(default=False)),
            ],
        ),
    ]
