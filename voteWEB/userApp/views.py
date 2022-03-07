from django.shortcuts import render, redirect
from.models import *

# Create your views here.

def loginPage(request):
    return render(request, 'user/login.html')

def donate(request):
    return render(request, 'user/donate.html')

def login(request):
    print('>>>> user login')
    if request.method == 'POST':
        print('>>>> request post')
        id = request.POST['id']
        pwd = request.POST['pwd']
        print('>>>> request param - ', id, pwd)
        context = {}
        try:
            user = WebMember.objects.get(member_id=id, member_pwd=pwd)

            request.session['member_name'] = user.member_name
            request.session['member_id'] = user.member_id

            context['session_member_name'] = request.session['member_name']
            context['session_member_id'] = request.session['member_id']
            # return render(request, 'index.html', context)
            return render(request, 'index.html', context)
        except Exception as e:
            context['error'] = 'invalid id, pwd'
            return render(request, 'user/donate.html', context)


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