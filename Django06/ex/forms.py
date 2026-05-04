from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import User, Tip
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password, check_password

class Register(ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username", "password", "confirm_password"]
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if username and len(username) < 5:
            self.add_error('username', 'Username must be minimum 5 characters.')
        if password and len(password) < 6:
            self.add_error('password', 'Password must be minimum 6 characters.')
        if password != confirm_password:
            self.add_error('confirm_password', 'The field confirmation does not match.')
        if User.objects.filter(username=username).exists():
            self.add_error('username', 'Username already exists..')

        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data["password"])

        if commit:
            print("====================")
            user.save()
        return user


class Login(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username", "password"]

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        
        user = User.objects.filter(username=username).first()
        if user is None:
            self.add_error('password', 'Invalid Username or Password!')
            return
        else:
            passwd = check_password(password, user.password)
            if passwd is False:
                self.add_error('password', 'Invalid Username or Password!')
        return cleaned_data
    

class Tips(ModelForm):
    content = forms.CharField(required=True)
    class Meta:
        model = Tip
        fields = ["content"]

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')

        return cleaned_data