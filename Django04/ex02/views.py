from django.shortcuts import render
from .forms import inputFrom
from django.http import HttpResponse
from django.shortcuts import redirect
from datetime import datetime
from django.conf import settings
# Create your views here.


# for tomorrow take the request and save it in the db
def saveText(request):
    if (request.method == "POST"):
        data = inputFrom(request.POST)
        if (data.is_valid()):
            with open(settings.LOG_FILE, "a") as file:
                file.write(data.cleaned_data["textField"] + ' - ' + str(datetime.now()) + "\n")
            return redirect("/ex02")
        else:
            return HttpResponse("ERROR!")

def renderForm(request):
    form = inputFrom()
    with open(settings.LOG_FILE, "r") as file:
        readfile = file.read()
        text_time = readfile.split("\n")
    return render(request, "form.html", {'form' : form, "text_time" : text_time})