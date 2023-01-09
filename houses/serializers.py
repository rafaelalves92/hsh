from rest_framework import serializers

from .models import House,SellHouse


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

class SellHouseSerializer(serializers.ModelSerializer):
        class Meta:
            model = SellHouse

            fields = [
                'id',
                'buyed_at',
                'house_id',
                'buyer_id',
             ]
            read_only_fields = ['house_id','buyer_id']

        




