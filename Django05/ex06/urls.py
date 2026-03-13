from django.urls import path
from . import views

urlpatterns = [
    path('init', views.create_table6),
    path('populate', views.insert_data6),
    path('display', views.display_data6),
    path('update', views.get_data2up),
    path('change', views.update_data),
]