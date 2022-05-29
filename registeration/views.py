from multiprocessing import context
from re import U
import django
from unicodedata import name
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.http import HttpResponse


#from registeration.models import User
from .models import User
from .models import Login
# Create your views here.


def Grad(request):
    return render(request, 'GraduationProject - Copy/Grad.html')


def signup(request):
    return render(request, 'GraduationProject - Copy/signup.html')


def login(request):
    return render(request, 'GraduationProject - Copy/login.html')


def log(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        bio = Login(username=username, password=password)
        bio.save()
        nam = User.objects.values_list('username')
        nam = list(sum(nam, ()))
        pas = User.objects.values_list('password')
        pas = list(sum(pas, ()))
        if username in nam and password in pas:
            return redirect('welcome2')
        else:
            return render(request, 'GraduationProject - Copy/login.html')


def user(request):
    if request.method == 'POST':
        x = request.POST.get('Username')
        y = request.POST.get('E-mail')
        w = request.POST.get('Password')
        z = request.POST.get('Degree of education')
        data = User(username=x, email=y, password=w, major=z)
        data.save()
        return redirect('welcome2')

    else:
        return render(request, 'GraduationProject - Copy/signup.html')


def forgotpass(request):
    return render(request, 'GraduationProject - Copy/forgotpass.html')


def welcome2(request):
    return render(request, 'GraduationProject - Copy/welcome2.html')


def processes(request):
    return render(request, 'GraduationProject - Copy/processes.html')


def rna(request):
    return render(request, 'GraduationProject - Copy/rna.html')


def dna(request):
    return render(request, 'GraduationProject - Copy/dna.html')


def protein(request):
    return render(request, 'GraduationProject - Copy/protein.html')


def profile(request):
    # if request.method == 'POST':
    username = request.POST.get('user')
    password = request.POST.get('pass')
    nam = User.objects.values_list('username')
    nam = list(sum(nam, ()))
    pas = User.objects.values_list('password')
    pas = list(sum(pas, ()))
    if username in nam and password in pas:
        return render(request, 'GraduationProject - Copy/profile.html')
    else:
        return render(request, 'GraduationProject - Copy/profile.html',
                      {'name': User.objects.get(password=1212121212)})
