from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import CommentsSerializer
from .models import Comments
from .permissions import isCommentOwner
from rest_framework_simplejwt.authentication import JWTAuthentication


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
