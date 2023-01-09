# Generated by Django 4.1.5 on 2023-01-06 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("houses", "0003_house_is_available"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="house",
            name="user",
        ),
        migrations.AddField(
            model_name="house",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="house",
            name="user_id",
            field=models.IntegerField(default=0),
        ),
    ]