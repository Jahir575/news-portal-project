"""counter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = "home"),
    path('contact/', views.contact, name = "contact"),
    path('details/<int:news_pk>', views.details, name= "details"),
    path('category/<int:news_pk>', views.category, name = "category"),
    path('about/', views.about, name = "about"),
    path('message/', views.message, name="message"),
    path('adminlogin/', views.adminlogin, name = 'adminlogin'),
    path('adminauth/', views.adminauth, name = 'adminauth'),
    path('adminloggedin/', views.adminloggedin, name = 'adminloggedin'),
    path('adminlogout/', views.adminlogout, name = 'adminlogout'),
    path('addemployee/', views.addemployee, name='addemployee'),
    path('employeelogin/', views.employeelogin, name='employeelogin'),
    path('employee_auth/', views.employee_auth, name='employee_auth'),
    path('loggedin_employee/', views.loggedin_employee, name = 'loggedin_employee'),

]

