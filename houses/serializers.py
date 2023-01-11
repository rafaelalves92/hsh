from rest_framework import serializers

from addresses.models import Address
from addresses.serializers import AddressSerializer
from users.models import User
from users.serializers import UserSerializer

from .models import House, LocationHouse,SellHouse


class HouseSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

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
            "is_active",
            "address",
            "user_id",
        ]

        read_only_fields = [
            "user_id",
        ]

    def create(self, validated_data):

        address_dict = validated_data.pop("address")
        address, _ = Address.objects.get_or_create(**address_dict)

        house_obj = House.objects.create(**validated_data, address=address)

        return house_obj


class HouseRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationHouse

        fields = [
            "id",
            "start_at",
            "finish_at",
            "house_id",
            "renter_id",
            "owner_id",
        ]

        read_only_fields = ["house_id", "renter_id", "owner_id"]

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
