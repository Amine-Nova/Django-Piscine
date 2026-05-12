from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path("articles", views.ArticleList.as_view(), name='articles_list'),
    path("publications", views.PublicationList.as_view(), name='publications_list'),
    path("favourite", views.FavouriteView.as_view(), name='favourite_list'),
    path("detail/<int:pk>/", views.DetailView.as_view(), name='detail'),
    path("publish", views.PublishForm.as_view(), name='publish_article'),
    path("addfav/<int:id>/", views.FavouriteAdd.as_view(), name='favourite_add'),
    path("login", views.LoginForm.as_view(), name='login_form'),
    path("register", views.RegisterForm.as_view(), name='register_form'),
    path("logout", views.Logout.as_view(), name='logout')
]