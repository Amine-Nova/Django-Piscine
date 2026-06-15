from django.urls import path
from . import views


urlpatterns = [
    path("", views.home),
    path("<str:room_name>/", views.chatroom, name="chatroom"),
    path("save", views.message_save)
]