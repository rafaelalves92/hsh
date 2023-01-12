from django.urls import path

from . import views

urlpatterns = [
    path("houses/create/", views.HouseCreateView.as_view()),
    path("houses/", views.HouseListView.as_view()),
    path("houses/<int:pk>", views.HouseDetailView.as_view()),
    path("houses/rent/", views.HouseLocationListView.as_view()),
    path("houses/<int:house_id>/rent/", views.HouseLocationCreateView.as_view()),
    path("houses/sell/", views.GetSellHouseView.as_view()),
    path("houses/<int:house_id>/sell/", views.SellHouseView.as_view()),
]
