from django.urls import path

from room import views

urlpatterns = [
    path("",views.rooms, name="rooms"),
    path("<slug:slug>/",views.room, name="room"),
]
