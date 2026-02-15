from django.shortcuts import render
from .forms import inputFrom
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Text
from datetime import datetime
# Create your views here.


# for tomorrow take the request and save it in the db
def saveText(request):
    if (request.method == "POST"):
        data = inputFrom(request.POST)
        if (data.is_valid()):
            text = data.cleaned_data['textField']
            db = Text(text=text, time=datetime.now())
            db.save()
            print(db)
            return HttpResponse("111111")
    else:
        return HttpResponse("hhhhhhhh")

def renderForm(request):
    form = inputFrom()
    return render(request, "form.html", {"form" : form})
