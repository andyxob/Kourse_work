from .models import Doctor
from django.forms import ModelForm, TextInput, Textarea
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ["name", "surname",'category', 'bio']
        widgets = {"name": TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Enter name"
        }),
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter surname"
            }),
            "category": TextInput(attrs={
                'class':'form-control',
                'placeholder':'enter category'}),
            "bio": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'enter bio'}),
        }

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name','last_name', 'password1', 'password2',]