from django.shortcuts import render, redirect

# Create your views here.

def candidate2(request):
    return render(request, 'candidate2/candidate2.html')
def detail(request):
    return render(request, 'candidate1/blog-two-details')
