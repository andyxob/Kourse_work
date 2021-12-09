from .models import Doctor, Meeting
from django.contrib.auth import get_user_model
from django import forms
#Check for unique email & username
non_alowed_usernames = ['abc']
User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control",
                                "placeholder":"Enter username"}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class":"form-control",
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


class MeetingForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop("user") or None
    #     super().__init__(*args, **kwargs)
    #     self.user = user

    doctor = forms.ModelChoiceField(widget=forms.Select({'class': 'form-control'}), queryset=Doctor.objects.all())
    class Meta:
        model = Meeting

        fields = ['doctor', "date", 'time', 'massage']

        widgets = {
            "date":forms.SelectDateWidget(attrs={'class':'form-control'}),
            "time": forms.Select(attrs={'class':'form-control'}),
            "massage":forms.Select(attrs={'class':'form-control'})
        }

    def clean(self, *args, **kwargs):
        cleaned_data = super().clean(*args, **kwargs)
        return cleaned_data

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

