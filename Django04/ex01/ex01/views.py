from django.shortcuts import render
# Create your views here.
def django(request):
    return render(request, "app/django.html")
def display(request):
    return render(request, "app/display.html")