# Generated by Django 5.0.2 on 2024-02-15 04:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0004_alter_borrowbookmodel_date_borrow"),
    ]

    operations = [
        migrations.AlterField(
            model_name="borrowbookmodel",
            name="book",
            field=models.ManyToManyField(blank=True, to="app.bookmodel"),
        ),
    ]
