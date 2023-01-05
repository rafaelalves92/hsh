from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAccountOwner
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