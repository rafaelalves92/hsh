from rest_framework import serializers
from .models import Comments


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments

        fields = [
            "id",
            "house_id",
            "description",
            "user_id",
        ]

        read_only_fields = [
            "user_id",
        ]

