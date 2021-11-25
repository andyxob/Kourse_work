from .models import Doctor
from django.forms import ModelForm, TextInput, Textarea

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

