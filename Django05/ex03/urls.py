from django.urls import path
from . import views
urlpatterns = [
    path('populate', views.insert_data3),
    path('display', views.display_data3)

]