from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm, get_user_model
from django import forms

from.models import Doctor
# Create your views here.

non_alowed_usernames = ['abc']
User = get_user_model()

@login_required
def meeting(request):
    return render(request, 'main/meeting.html')


def index(request):
    doctors = Doctor.objects.all()
    return render(request, 'main/index.html',{'title':'Main page', 'Doctors':doctors})

def about(request):
    return render(request, 'main/about.html')


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password1 = form.cleaned_data.get("password1")
        password2 = form.cleaned_data.get("password2")
        try:
            user = User.objects.create_user(username, email, password1)
        except:
            user = None
        if user != None:
            # request.user == user
            # user is valid and active -> is_active
            login(request, user)
            return redirect("main")
        else:
            request.session['registration_error'] = 1  # 1 ==True

    return render(request, "accounts/signup.html", {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user != None:
            # request.user == user
            # user is valid and active -> is_active
            login(request, user)
            return redirect("main")
        else:

            request.session['invalid_user'] = 1  # 1 ==True

    return render(request, "accounts/login.html", {'form': form})

def logout_view(request):
    logout(request)
    #request.user == Anon User
    return redirect("/login")

class About:

    def doctors(request):
        doctors = Doctor.objects.all()
        return render(request, 'main/about/doctors.html', {'title': 'Doctors', 'Doctors': doctors})

    def massages(request):
        return render(request, 'main/about/massage.html')

    def massage_back(request):
        return render(request, 'main/about/massages/back.html')

    def massage_neck(request):
        return render(request, 'main/about/massages/neck.html')

    def massage_manual(request):
        return render(request, 'main/about/massages/manual_therapy.html')

    def massage_anti(request):
        return render(request, 'main/about/massages/anti-cellulite.html')



