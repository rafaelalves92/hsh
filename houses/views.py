from .models import House, LocationHouse,SellHouse
from .serializers import HouseSerializer, HouseRentSerializer,SellHouseSerializer
from .permissions import isHouseOwner, IsHouseOwnerOrRenter
from rest_framework.views import Response, status, Request
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotAcceptable




class HouseView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = HouseSerializer
    queryset = House.objects.all()

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


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
        return LocationHouse.objects.filter(renter_id=self.request.user.id)


class SellHouseView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SellHouseSerializer
    queryset = SellHouse.objects.all()

    def perform_create(self, serializer):
        house_id = self.kwargs['house_id']
        house_obj = get_object_or_404(House, pk=house_id)
        if not house_obj.is_available:
            raise NotAcceptable("This house is not avaiable")
    

        house_obj.is_available = False
        house_obj.user_id = self.request.user.id

        house_obj.save()

        serializer.save(house = house_obj,buyer = self.request.user)


class GetSellHouseView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SellHouseSerializer
    queryset = SellHouse.objects.all()

    def get_queryset(self):
        return SellHouse.objects.filter(buyer_id = self.request.user.id)