from django.urls import path
from . import views

urlpatterns = [
    path('init', views.create_table8),
    path('populate', views.copy_data8),
    path('display', views.display_data8)
]