from django.urls import path
from . import views
urlpatterns = [
    path('init', views.create_table2),
    path('populate', views.insert_data2),
    path('display', views.display_data),
    # path('display')
]
