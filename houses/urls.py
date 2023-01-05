from django.urls import path

from . import views

urlpatterns = [
    path("houses/", views.HouseView.as_view()),
    path("houses/<int:pk>", views.HouseDetailView.as_view()),
    path("houses/<int:house_id>/rent/", views.HouseLocationView.as_view()),
]
