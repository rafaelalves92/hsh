from django.urls import path

from . import views

urlpatterns = [
    path("houses/sell/",views.SellHouseView.as_view()),
    path("houses/<int:house_id>/sell/",views.SellHouseView.as_view()),
]
