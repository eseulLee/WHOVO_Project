from django.shortcuts import render, redirect
from.models           import *

# Create your views here.

def index(request):
    return render(request, 'index.html')
def loginPage(request):
    return render(request,'login.html')

def login(request):
    print('>>>> user login')
    if request.method == 'GET':
        return redirect('whovo')
    else :
        print('>>>> request POST')
        id = request.POST['id']
        pwd = request.POST['pwd']
        print('>>>> request param - ', id , pwd)
        user = WebMember.objects.get(member_id=id, member_pwd=pwd)
        print('>>>> user result', user)
        context = {}
        if user is not None :
            request.session['member_id'] = user.member_id
            request.session['member_name'] = user.member_name
            context['id'] = request.session['member_id']
            context['name'] = request.session['member_id']

            return render(request, 'donate.html', context)
        else :
            return redirect('whovo')


def joinForm(request) :
    return render(request, 'joinForm.html')

def join(request):
    print('>>>> user join - ')
    id = request.POST['id']
    pwd = request.POST['pwd']
    name = request.POST['name']
    poli = request.POST['poli']
    age = request.POST['age']
    print('>>>> param values - ', id, pwd, name,poli,age)
    WebMember(member_id=id, member_pwd=pwd, member_name=name, member_poli=poli,member_age=age).save()
    return redirect('whovo')

def logout(request) :
    print(">>>> user logout")
    request.session['member_name'] = {}
    request.session['member_id'] = {}
    request.session.modified = True
    return redirect('whovo')

def blog(request) :
    return render(request, 'blog.html')

def candidate1(request):
    return render(request, 'candidate1.html')

def candidate2(request):
    return render(request, 'candidate2.html')

def candidate3(request):
    return render(request, 'candidate3.html')

def blogDetail(request):
    return render(request, 'blog-two-details.html')

def donate(request):
    return render(request, 'donate.html')

def events(request):
    return render(request, 'events.html')