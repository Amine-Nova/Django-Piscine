from django.shortcuts import render, redirect
from django.views import generic
from . import models
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from datetime import datetime
from django import forms


# Create your views here.


class ArticleList(generic.ListView):
    model = models.Article
    template_name = "index.html"
    context_object_name = "object_list"

    def get_queryset(self):
        return models.Article.objects.order_by('-created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_form'] = AuthenticationForm()
        return context


class PublicationList(generic.ListView):
    model = models.Article
    template_name = "publications.html"
    context_object_name = "object_list"

    def get_queryset(self):
        return models.Article.objects.order_by('-created')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated is False:
            return redirect('articles:home')
        return super().dispatch(request, *args, **kwargs)

class DetailView(generic.DetailView):
    model = models.Article
    template_name = "details.html"
    context_object_name = "object_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_form'] = AuthenticationForm()
        return context

class FavouriteView(generic.ListView):
    model = models.UserFavouriteArticle
    template_name = "favourite.html"
    context_object_name = "object_list"

class Home(generic.RedirectView):
    pattern_name = 'articles:articles_list'

class LoginForm(LoginView):
    template_name = 'login.html'
    next_page = 'articles:home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_form'] = AuthenticationForm()
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('articles:home')
        return super().dispatch(request, *args, **kwargs)

class RegisterForm(generic.CreateView):
    template_name = "register.html"
    model = models.User
    form_class = UserCreationForm
    success_url = reverse_lazy("articles:login_form")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_form'] = AuthenticationForm()
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('articles:home')
        return super().dispatch(request, *args, **kwargs)


class FavouriteAdd(generic.CreateView):
    model = models.UserFavouriteArticle
    fields = []
    success_url = reverse_lazy("articles:publications_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.article = models.Article.objects.get(id=self.kwargs['id'])
        return super().form_valid(form)


class PublishForm(generic.CreateView):
    template_name = 'publish.html'
    model = models.Article
    fields = ['title', 'synopsis', 'content']
    success_url = reverse_lazy("articles:publish_article")


    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.created = datetime.now()
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated is False:
            return redirect('articles:home')
        return super().dispatch(request, *args, **kwargs)


class Logout(LogoutView):
    next_page = 'articles:home'
