from django.shortcuts import render, redirect
from.models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')


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
        # insert into table(id, pwd, name) values('','','')
        # orm : modelName(attr - value).save()
    WebMember(member_id=id, member_pwd=pwd, member_name=name, member_poli=poli,member_age=age).save()
    # return render(request , 'user/index.html')
    return redirect('bbs_index')
