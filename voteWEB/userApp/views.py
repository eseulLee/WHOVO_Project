from django.shortcuts import render

# Create your views here.
def donate(request):
    return render(request, 'user/donate.html')

def loginPage(request):
    return render(request,'user/login.html')
