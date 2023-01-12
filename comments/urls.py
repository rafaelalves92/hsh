from django.urls import path

from . import views

urlpatterns = [
    path("comments/", views.CommentsView.as_view()),
    path("comments/<int:pk>", views.CommentsDetailView.as_view()),
    path("comments/house/<int:house_id>", views.CommentsHouseView.as_view()),
    path("comments/user/<int:user_id>", views.CommentsUserView.as_view()),
]
