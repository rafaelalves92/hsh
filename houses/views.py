from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotAcceptable
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.views import Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import House, LocationHouse, SellHouse
from .permissions import IsHouseOwnerOrRenter, isHouseOwner
from .serializers import HouseRentSerializer, HouseSerializer, SellHouseSerializer


class HouseCreateView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    serializer_class = HouseSerializer
    queryset = House.objects.all()

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


class HouseListView(ListAPIView):
    serializer_class = HouseSerializer
    queryset = House.objects.all()


class HouseDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, isHouseOwner]

    serializer_class = HouseSerializer
    queryset = House.objects.all()

    def delete(self, request: Request, pk: int) -> Response:
        house_obj = get_object_or_404(House, pk=pk)

        self.check_object_permissions(request, house_obj)
        self.object = self.get_object()
        self.object.soft_delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class HouseLocationCreateView(CreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsHouseOwnerOrRenter]

    serializer_class = HouseRentSerializer

    def perform_create(self, serializer):

        house_id = self.kwargs["house_id"]
        house_obj = get_object_or_404(House, pk=house_id)

        self.check_object_permissions(self.request, house_obj)

        if not house_obj.is_available:
            raise NotAcceptable("This house is not avaiable")

        house_obj.is_available = False
        house_obj.save()

        serializer.save(
            house=house_obj,
            renter=self.request.user,
            owner_id=house_obj.user_id,
            location_price=house_obj.location_price,
        )


class HouseLocationListView(ListAPIView):
    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAuthenticated, IsHouseOwnerOrRenter]

    queryset = LocationHouse.objects.all()
    serializer_class = HouseRentSerializer

    def get_queryset(self):
        return LocationHouse.objects.filter(renter_id=self.request.user.id)


class SellHouseView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SellHouseSerializer
    queryset = SellHouse.objects.all()

    def perform_create(self, serializer):
        house_id = self.kwargs["house_id"]
        house_obj = get_object_or_404(House, pk=house_id)
        if not house_obj.is_available:
            raise NotAcceptable("This house is not avaiable")

        house_obj.is_available = False
        house_obj.user_id = self.request.user.id

        house_obj.save()

        serializer.save(
            house=house_obj,
            buyer=self.request.user,
            owner_id=house_obj.user_id,
            sell_price=house_obj.sell_price,
        )


class GetSellHouseView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SellHouseSerializer
    queryset = SellHouse.objects.all()

    def get_queryset(self):
        return SellHouse.objects.filter(buyer_id=self.request.user.id)
