from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import CommentsSerializer
from .models import Comments
from .permissions import isCommentOwner
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView, Request, Response


class CommentsView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


class CommentsDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, isCommentOwner]

    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()


class CommentsHouseView(ListAPIView):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()

    def get_queryset(self):
        house_id = self.kwargs["house_id"]

        return Comments.objects.filter(house_id=house_id)


class CommentsUserView(ListAPIView):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()

    def get_queryset(self):
        user_id = self.kwargs["user_id"]

        return Comments.objects.filter(user_id=user_id)
