from django.shortcuts import render, redirect

# Create your views here.

def candidate1(request):
    return render(request,'candidate1/candidate1.html')

def detail01(request) :
    return render(request, 'candidate1/blogDetail1.html')