# Generated by Django 4.1.5 on 2023-01-04 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("houses", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="house",
            name="is_available",
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
