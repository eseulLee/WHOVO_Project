from django.shortcuts import render, redirect
from.models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def joinForm(request) :
    return render(request, 'joinForm.html')