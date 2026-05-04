from django.urls import path
from . import views


urlpatterns = [
    path("", views.home),
    path("register", views.register_page),
    path("login", views.login_page),
    path("random", views.getRandom),
    path("logout", views.logout),
    path("delete/<int:id>/", views.delete, name='delete_tip'),
    path("up/<int:id>/", views.upVote, name='upvote'),
    path("down/<int:id>/", views.downVote, name='downvote')
]
