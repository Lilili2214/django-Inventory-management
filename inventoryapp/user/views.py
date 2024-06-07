from django.shortcuts import render, redirect
from .forms import LoginForm, UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
# Create your views here.



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-index')
    else:
        form= UserCreationForm()
    context= {'form': form}
    return render(request, 'user/register.html', context)



def mylogin(request):
    form = LoginForm()
    if request.method =='POST':
        form= LoginForm(request, data= request.POST)
        if form.is_valid():
            username= request.POST.get('username')
            password= request.POST.get('password')
            user = authenticate(request, username= username, password= password)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard-index")
    context= {'form' : form}
    return render(request, 'user/login.html', context=context)



def logout(request):
    auth.logout(request)
    return redirect("home")