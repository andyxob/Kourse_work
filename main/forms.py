from django.http import request

from .models import Doctor, Result
from django.forms import ModelForm, TextInput, Textarea, EmailInput, ChoiceField

from django.contrib.auth import get_user_model
from django import forms
#Check for unique email & username

non_alowed_usernames = ['abc']
User = get_user_model()



class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=TextInput(attrs={"class": "form-control",
                                "placeholder":"Enter username"}))
    email = forms.EmailField(
        widget=EmailInput(attrs={"class":"form-control",
                                 "placeholder":"Enter e-mail"}))
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control",
                                          "id": "user-password",
                                          "placeholder":"Enter password"}))

    password2 = forms.CharField(
        label= "Confirm Password",
        widget=forms.PasswordInput(attrs={"class": "form-control",
                                          "id": "user-confirm-password",
                                          "placeholder":"Confirm password"})
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if username in non_alowed_usernames:
            raise forms.ValidationError("This is an invalid username, please pick another")
        if qs.exists():
            raise forms.ValidationError("This is an invalid username, please pick another")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This email is already in use")
        return email

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control",
                                                             "placeholder": "Enter username"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control",
                                          "id": "user-password",
                                          "placeholder":"Enter Password"})
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError("This is an invalid user")
        return username


class MeetingForm(forms.Form):
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all())
    date = forms.DateTimeField(widget= forms.SelectDateWidget)
    time = forms.TimeField()

    class Meta:
        model = Result


# class DoctorForm(ModelForm):
#     class Meta:
#         model = Doctor
#         fields = ["name", "surname",'category', 'bio']
#         widgets = {"name": TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': "Enter name"
#         }),
#             "surname": TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': "Enter surname"
#             }),
#             "category": TextInput(attrs={
#                 'class':'form-control',
#                 'placeholder':'enter category'}),
#             "bio": Textarea(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'enter bio'}),
#         }

