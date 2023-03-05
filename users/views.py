from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import *
def loginPage(request):

    if request.user.is_authenticated:
        return redirect('store')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)

        except:
            pass

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('store')

    return render(request, 'users/login.html')


def logoutPage(request):
        logout(request)

        return redirect('login')


def registerPage(request):
    form = customUserCreationForm()
    
    if request.method == 'POST':
        form = customUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)
            return redirect('store')



    context = {'form': form}
    return render(request, 'users/register.html', context)
