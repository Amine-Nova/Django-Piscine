from django.urls import path
from . import views

urlpatterns = [
    path('', views.renderForm),
    path('save', views.saveText)
]
