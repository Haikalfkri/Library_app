# Generated by Django 5.0.2 on 2024-02-16 14:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0007_alter_borrowbookmodel_user_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="borrowbookmodel",
            name="date_return",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
