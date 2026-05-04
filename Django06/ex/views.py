from django.shortcuts import render, redirect
from django.conf import settings
import random
from django.http import JsonResponse
from . import forms
from .models import User, Tip, Vote, Perm
from django.contrib.auth import authenticate, login

# Create your views here.

def count_points():
    users = User.objects.all()
    for user in users:
        tips = Tip.objects.filter(author=user.username)
        user.points = 0
        for tip in tips:
            if tip.upvote > 0:
                user.points += tip.upvote * 5
            if tip.downvote > 0:
                user.points += tip.downvote * -2
        user.save() 
    return   

def has_permission(user: User, perm_id: int):
    if User.objects.filter(username=user.username, perm=Perm.objects.get(id=perm_id)).exists():
        return True
    return False

def set_perm(user: User, perm_id: int):
    perm = Perm.objects.get(id=perm_id)
    user.perm.add(perm)

def getRandom(request):
    name = random.choice(settings.RANDOM_NAMES)
    data = {
        'name' : name 
    }
    return JsonResponse(data)
    
def add_permissions(user: User):
    user_points = user.points
    user.perm.clear()
    if user_points >= 15:
        set_perm(user, 2)
    if user_points >= 30:
        set_perm(user, 1)
    print(user.perm.values_list())

def home(request):
    tips = Tip.objects.all()
    if request.session.get('logged_in', False):
        user = User.objects.get(username=request.session['username'])
        count_points()
        print(len(user.perm.values()))
        add_permissions(User.objects.get(username=request.session['username']))
    if request.method == 'POST':
        form = forms.Tips(request.POST)
        if form.is_valid():
            add = form.save(commit=False)
            add.author = request.session['username']
            add.save()
            return redirect('/')
        return render(request, "index.html", {'form': form, 'tips': tips, 'perms': user.perm.values()})
    name = random.choice(settings.RANDOM_NAMES)
    form = forms.Tips()
    if request.session.get('logged_in', False):
        return render(request, "index.html", {'name' : name, 'form': form, 'tips': tips, 'perms': user.perm.values()})
    else:
        return render(request, "index.html", {'name' : name, 'form': form, 'tips': tips})

def login_page(request):
    if request.session.get('logged_in', False):
        return redirect('/')
    else:
        if request.method == 'POST':
            name = random.choice(settings.RANDOM_NAMES)
            form = forms.Login(request.POST)
            if form.is_valid():
                request.session['logged_in'] = True
                request.session['username'] = request.POST.get("username")
                return redirect('/')
            return render(request, "login.html", {'name' : name, 'form': form})
        name = random.choice(settings.RANDOM_NAMES)
        form = forms.Login()
        return render(request, "login.html", {'name' : name, 'form': form})

def register_page(request):
    if request.session.get('logged_in', False):
        return redirect('/')
    else:
        if request.method == 'POST':
            name = random.choice(settings.RANDOM_NAMES)
            form = forms.Register(request.POST)
            if form.is_valid():
                form.save()
                request.session['logged_in'] = True
                request.session['username'] = request.POST.get("username")
                return redirect('/')
            return render(request, "registration.html", {'name' : name, 'form': form})
        name = random.choice(settings.RANDOM_NAMES)
        form = forms.Register()
        return render(request, "registration.html", {'name' : name, 'form': form})


def logout(request):
    request.session['logged_in'] = False
    return redirect('/')

def delete(request, id):
    user = User.objects.get(username=request.session['username'])
    tip = Tip.objects.get(id=id)
    perm = has_permission(user, 1)
    if tip.author == user.username or perm:
        tip.delete()
    return redirect("/")


def upVote(request, id):
    user = User.objects.get(username=request.session['username'])
    tip = Tip.objects.get(id=id)
    vote_check = Vote.objects.filter(tip=tip, user=user).first()
    if vote_check == None:
        vote = Vote(user=user, tip=tip, value=1)
        tip.upvote += 1
        vote.save()
        tip.save()
    elif vote_check:
        if vote_check.value == 1:
            tip.upvote -= 1
            vote_check.delete()
            tip.save()
        elif vote_check.value == 0:
            tip.upvote +=1
            tip.downvote -= 1
            vote_check.value = 1
            vote_check.save()
            tip.save()
    return redirect("/")

def downVote(request, id):
    user = User.objects.get(username=request.session['username'])
    tip = Tip.objects.get(id=id)
    vote_check = Vote.objects.filter(tip=tip, user=user).first()      
    if vote_check == None and (tip.author == user.username or has_permission(user, 2)):
        vote = Vote(user=user, tip=tip, value=0)
        tip.downvote +=1
        vote.save()
        tip.save()
    elif vote_check:
        if vote_check.value == 0:
            tip.downvote -= 1
            vote_check.delete()
            tip.save()
        elif vote_check.value == 1 and (tip.author == user.username or has_permission(user, 2)):
            tip.downvote +=1
            tip.upvote -=1
            vote_check.value = 0
            vote_check.save()
            tip.save()
    return redirect("/")