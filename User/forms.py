from django import forms
from User.models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm

class CreateUser(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Again password')
    
    class Meta(UserCreationForm):
        model = Newuser
        fields = ('username','email','password1','password2','img')

class LoginUser(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Password')

    class Meta(AuthenticationForm):
        model = Newuser
        fields = ('username','password')
