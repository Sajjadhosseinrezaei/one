from django.shortcuts import render , redirect
from .forms import UserregistrationsForm , LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout

# Create your views here.
def user_register(request):
    if request.method == 'POST':
        form = UserregistrationsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if User.objects.filter(username = cd['username']).first():
                messages.error(request, "This username is already taken")
                return redirect('home')
            else:
                User.objects.create_user(cd['username'], cd['email'], cd['password'])
                messages.success(request, 'user regiser shod bro admin pannel')
                return redirect('home')
    else:
        form = UserregistrationsForm()
        return render(request, 'register.html', {'form':form})
    

def loggin_form(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password = cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'user loggin successfully', 'success')
                return redirect('home')
            else:
                messages.error(request,'username or password is wrong','danger')
    else:
        form = LoginForm()
    return render(request, 'loggin.html', {'form':form})

def logout_form(request):
    logout(request)
    messages.success(request,'user loggout', 'success')
    return redirect('home')

    

