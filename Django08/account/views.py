from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_POST


def home(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
    else:
        context = {}
        context['form'] = AuthenticationForm()
    return render(request, "account/account.html", context) 

@require_POST
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse(
            {"message": "Login successful"},
            status=200
        )
        else:
            return JsonResponse(
                {"message": "Invalid credentials"},
                status=401
            )

def logout_user(request):
    if request.method == "POST":
        state = logout(request)
        print(state)
        
        return JsonResponse({"message": "Logout successful"}, status=200)