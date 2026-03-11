from django.urls import path
from . import views

urlpatterns = [
    path('init', views.create_table4),
    path('populate', views.insert_data4),
    path('display', views.display_data4),
]