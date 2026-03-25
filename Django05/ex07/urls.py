from django.urls import path
from . import views

urlpatterns = [
    path('populate', views.insert_data7),
    path('display', views.display_data7),
    path('update', views.get_data2up7),
    path('change', views.update_data7),
]