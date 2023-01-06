from .models import House
from .serializers import HouseSerializer
from .permissions import isHouseOwner
from rest_framework.views import Response, status, Request
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404


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
