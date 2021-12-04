from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.template.defaulttags import firstof

from .forms import LoginForm, RegisterForm, get_user_model, MeetingForm
from django import forms

from.models import Doctor,Result
# Create your views here.

non_alowed_usernames = ['abc']
User = get_user_model()

@login_required(login_url='login/')
def meeting(request):
    doctors = Doctor.objects.all()
    username = request.user.username
    form = MeetingForm(request.POST or None)
    if form.is_valid():

        new_meeting = form.save()
        return redirect('main')
    return render(request, 'main/meeting.html', {'title':'Запис',
                                                 'username':username,
                                                 'form':form})




@login_required(login_url='login/')
def profile(request):
    username = request.user.username
    results = Result.objects.all()
    return render(request, 'accounts/profile.html', {'username':username, 'resulrs':results})

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
        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
            except:
                user = None
            if user != None:
                # request.user == user
                # user is valid and active -> is_active
                login(request, user)
                return redirect("profile")
            else:
                request.session['registration_error'] = 1  # 1 ==True

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
            return redirect("profile")
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



