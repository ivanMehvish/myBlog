from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post

class postForm(forms.ModelForm):

    class Meta:
        model=Post
        fields=('title', 'desc','text')




class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=15, widget=forms.PasswordInput)
    

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2'] 