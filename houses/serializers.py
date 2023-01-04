from rest_framework import serializers

from .models import House


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House

        fields = [
            "id",
            "bedrooms",
            "rooms",
            "suits",
            "kitchens",
            "bathrooms",
            "toilets",
            "land_area",
            "parking_spaces",
            "sell_price",
            "location_price",
            "description",
            "is_available",
        ]
