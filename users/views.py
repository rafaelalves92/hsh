from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Request, Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from houses.models import House
from houses.serializers import HouseSerializer

from .models import User
from .permissions import IsAccountOwner, IsHouseOwner
from .serializers import UserSerializer


class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAuthenticated, IsAccountOwner]

    serializer_class = UserSerializer
    queryset = User.objects.all()

    lookup_url_kwarg = "pk"


class UserHousesDetailView(APIView):
    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAuthenticated, IsHouseOwner]

    queryset = House.objects.all()
    serializer_class = HouseSerializer

    def get(self, request: Request, id) -> Response:
        house = House.objects.filter(user_id=id)

        self.check_object_permissions(request, house)

        serializer = HouseSerializer(house, many=True)

        return Response(serializer.data)
