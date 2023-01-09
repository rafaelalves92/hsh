from django.urls import path

from . import views

urlpatterns = [
     path("houses/<int:house_id>/sell/",views.SellHouseView.as_view()),
]
