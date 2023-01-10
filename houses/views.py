from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotAcceptable
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import House, LocationHouse
from .permissions import IsHouseOwnerOrRenter
from .serializers import HouseRentSerializer, HouseSerializer


class HouseView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = HouseSerializer
    queryset = House.objects.all()


class HouseDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = HouseSerializer
    queryset = House.objects.all()

    # Só falta fazer o soft delete


class HouseLocationView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsHouseOwnerOrRenter]

    serializer_class = HouseRentSerializer
    queryset = House.objects.all()

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
        )

    def get_queryset(self):
        if self.request.user.is_superuser:
            return LocationHouse.objects.filter(owner_id=self.request.user.id)
        else:
            return LocationHouse.objects.filter(renter_id=self.request.user.id)
