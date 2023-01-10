from django.urls import path

from . import views

urlpatterns = [
    path("comments/", views.CommentsView.as_view()),
    path("comments/<int:pk>", views.CommentsDetailView.as_view()),
]
