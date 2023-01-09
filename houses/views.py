from django.shortcuts import get_object_or_404
from .serializers import SellHouseSerializer
from rest_framework import generics
from .models import SellHouse,House
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated


class SellHouseView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    serializer_class = SellHouseSerializer
    queryset = SellHouse.objects.all()
    def perform_create(self, serializer):
        house_id = self.kwargs['house_id']
        house_obj = get_object_or_404(House,pk = house_id)
        serializer.save(house = house_obj,buyer = self.request.user)


    def get_queryset(self):
        return SellHouse.objects.filter(buyer_id = self.request.user.id)

