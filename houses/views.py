from .models import House
from .serializers import HouseSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class HouseView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = HouseSerializer
    queryset = House.objects.all()

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


class HouseDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = HouseSerializer
    queryset = House.objects.all()

    # Só falta fazer o soft delete
