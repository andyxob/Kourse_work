from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from cabinet.accounts.forms import *
# Create your views here.

def register_view(request):
    form = RegisterForm(request.post or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password1 = form.cleaned_data.get("password1")
        password2 = form.cleaned_data.get("password2")
        user = User.objects.create_user(username, email, password)
        try:
            user = User.objects.create_user(username, email, password)
        except:
            user = None
        if user != None:
            # request.user == user
            # user is valid and active -> is_active
            login(request, user)
            return redirect("/")
        else:
            request.session['registration_error'] = 1  # 1 ==True

    return render(request, "signup.html", {'form': form})

def login_view(request):
    form = LoginForm(request.post or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user != None:
            # request.user == user
            # user is valid and active -> is_active
            login(request, user)
            return redirect("/")
        else:

            request.session['invalid_user'] = 1  # 1 ==True

    return render(request, "login.html", {'form': form})

def logout_view(request):
    logout(request)
    #request.user == Anon User
    return redirect("/login")