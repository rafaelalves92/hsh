from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import House
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

        serializer.save(house=house_obj, renter=self.request.user)
