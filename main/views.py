from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from.forms import DoctorForm, SignUpForm
from.models import Doctor
# Create your views here.

def index(request):
    doctors = Doctor.objects.all()
    return render(request, 'main/index.html',{'title':'Main page', 'Doctors':doctors})

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

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect("{% url 'main' %}")
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})


