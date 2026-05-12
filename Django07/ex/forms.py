from django import forms
from django.forms import ModelForm
from .models import User
from django.contrib.auth.forms import AuthenticationForm

# class Login(ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     class Meta:
#         model = User
#         fields = ["username", "password"]

#     def clean(self):
#         cleaned_data = super().clean()
#         username = cleaned_data.get('username')
#         password = cleaned_data.get('password')

        
#         user = User.objects.filter(username=username, password=password).first()
#         if user is None:
#             self.add_error('password', 'Invalid Username or Password!')
#             return
#         return cleaned_data