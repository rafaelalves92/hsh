from django.db import models


class House(models.Model):
    bedrooms = models.IntegerField()
    rooms = models.IntegerField()
    suits = models.IntegerField()
    kitchens = models.IntegerField()
    bathrooms = models.IntegerField()
    toilets = models.IntegerField()
    land_area = models.IntegerField()
    parking_spaces = models.IntegerField()
    sell_price = models.FloatField()
    location_price = models.FloatField()
    description = models.CharField(max_length=250)
    is_available = models.BooleanField()
    user_id = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    address = models.OneToOneField(
        "addresses.Address",
        on_delete=models.CASCADE,
        related_name="address",
    )

    buyers = models.ManyToManyField(
        "users.User",
        through="houses.SellHouse",
        related_name="buyed_houses",
    )

    renters = models.ManyToManyField(
        "users.User",
        through="houses.LocationHouse",
        related_name="rented_houses",
    )

    def soft_delete(self):
        self.is_active = False
        self.save()


class SellHouse(models.Model):
    buyed_at = models.DateTimeField(auto_now_add=True)

    house = models.ForeignKey(
        "houses.House",
        on_delete=models.CASCADE,
        related_name="house_sold",
    )

    buyer = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="buyer_house",
    )


class LocationHouse(models.Model):
    start_at = models.DateField()
    finish_at = models.DateField()
    owner_id = models.IntegerField()

    house = models.ForeignKey(
        "houses.House",
        on_delete=models.CASCADE,
        related_name="house_rented",
    )

    renter = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="renter_house",
    )
