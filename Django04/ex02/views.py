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
            file = open(settings.LOG_FILE, "a+")
            # text = 'amieneee'
            file.write("amineeee")
            file.close
            print(file)
            return HttpResponse("file created")
    else:
        return HttpResponse("hhhhhhhh")

def renderForm(request):
    form = inputFrom()
    return render(request, "form.html", {'form' : form})