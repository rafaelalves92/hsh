from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
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


class CommentsHouseView(APIView):
    def get(self, request: Request, house_id: int) -> Response:
        comments = Comments.objects.filter(house_id=house_id)
        serializer = CommentsSerializer(comments, many=True)

        return Response(serializer.data)


class CommentsUserView(APIView):
    def get(self, request: Request, user_id: int) -> Response:
        comments = Comments.objects.filter(user_id=user_id)
        serializer = CommentsSerializer(comments, many=True)

        return Response(serializer.data)
