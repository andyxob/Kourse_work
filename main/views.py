from django.shortcuts import render, redirect
from.forms import DoctorForm
from.models import Doctor
from django.contrib.auth import authenticate, login, logout
from cabinet.accounts.forms import LoginForm, RegisterForm, User

# Create your views here.


def index(request):
    doctors = Doctor.objects.all()
    return render(request, 'main/index.html',{'title':'Main page', 'Doctors':doctors})

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

class About:

    def about(request):
        return render(request, 'main/about.html')

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

def doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'main/about/doctors.html', {'title': 'Doctors', 'Doctors': doctors})

def massages(request):
    return render(request, 'main/about/massage.html',)

def create(request):
    error = ''
    if request.method =='POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error ='Form was not valid'

    form = DoctorForm()
    context = {'form': form,
               'error': error
               }
    return render(request, 'main/about/doctors.html', context)

