from django.shortcuts import render
from django import http
# Create your views here.

def start(request):
    return http.HttpResponse("start")