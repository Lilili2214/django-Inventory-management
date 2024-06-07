from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

from django import forms
from django.contrib.auth.forms import AuthenticationForm


from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.forms import UserCreationForm




class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model= User
        fields=['username', 'password1','password2']

   

class LoginForm(AuthenticationForm):
    username= forms.CharField(widget=TextInput())
    password= forms.CharField(widget=PasswordInput())



class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields= '__all__'