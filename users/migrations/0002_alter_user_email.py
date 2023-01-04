# Generated by Django 4.1.5 on 2023-01-04 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                error_messages={"unique": "This field must be unique."},
                max_length=254,
                unique=True,
            ),
        ),
    ]
