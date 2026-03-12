from django.urls import path
from . import views

urlpatterns = [
    path('populate', views.insert_data5),
    path('display', views.display_data5),
    path('remove', views.select_todelete5),
    path('delete', views.delete_movie5),
]
