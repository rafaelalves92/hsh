from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = [
            "id",
            "name",
            "email",
            "password",
            "phone_number",
            "city",
            "district",
            "is_superuser",
        ]

        extra_kwargs = {"password": {"write_only": True}}
