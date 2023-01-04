from rest_framework.views import APIView, status, Response, Request
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import House
from .serializers import HouseSerializer
from django.shortcuts import get_object_or_404


class HouseView(APIView):
    def get(self, request: Request) -> Response:
        houses = House.objects.all()

        serializer = HouseSerializer(houses, many=True)

        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = HouseSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

class HouseDetailView(APIView):
    ...
