"""cabinet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [

    path('', views.index,name = 'main'),
    path('about', views.about, name='about'),
    path('create', views.create, name = 'create'),
    path('doctors', views.doctors, name='doctors'),
    path('massages', views.massages, name='massages'),
    path('massage_back', views.massage_back, name='massage_back'),
    path('massage_neck', views.massage_neck, name='massage_neck'),
    url(r'^signup/$', views.signup, name='signup'),


    #path('doctors', views.about_doctors, name='doctors'),
]
