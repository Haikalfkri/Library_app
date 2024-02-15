# Generated by Django 5.0.2 on 2024-02-15 02:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_bookmodel"),
    ]

    operations = [
        migrations.CreateModel(
            name="BorrowBookModel",
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
                ("quantity", models.PositiveIntegerField(default=1)),
                ("adress", models.TextField()),
                ("date_borrow", models.DateTimeField(auto_now_add=True)),
                ("date_return", models.DateTimeField()),
                ("user_image", models.ImageField(upload_to="user_images/")),
                ("book", models.ManyToManyField(to="app.bookmodel")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
