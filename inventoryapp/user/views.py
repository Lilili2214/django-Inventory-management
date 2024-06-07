from django.shortcuts import render, redirect
from .forms import LoginForm, UserCreationForm, UpdateProfileForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth, User
# Create your views here.
from .models import Profile
from django.contrib.auth.decorators import login_required

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

@login_required
def profile(request, pk):
    user =User.objects.get(id=pk)
    profile = user.profile
    context= {'profile': profile}
    return render(request, 'user/profile.html')



def profile_update(request, pk):
    user =User.objects.get(id=pk)
    profile = user.profile
    
    form = UpdateProfileForm(instance=profile)
    if request.method=='POST':
        form= UpdateProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user-profile',pk= pk)

    context={
        'formupdate':form
    }
    return render(request, 'user/profile_update.html', context)

