from rest_framework import generics
from rest_framework.views import APIView, Request, Response
from .models import User
from .serializers import UserSerializer
from houses.models import House
from houses.serializers import HouseSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAccountOwner, IsHouseOwner
from rest_framework.permissions import IsAuthenticated

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

    permission_classes = [ IsAuthenticated, IsHouseOwner]

    def get(self, request: Request, id) -> Response:
        house= House.objects.filter(user_id = id)
        
        self.check_object_permissions(request, house)

        serializer = HouseSerializer(house, many=True)

        return Response(serializer.data)
        








