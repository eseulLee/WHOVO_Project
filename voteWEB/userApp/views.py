from django.shortcuts import render, redirect
from .models          import *
from bbsApp.models    import Post


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
            context['error'] = '아이디 또는 비밀번호를 잘못 입력했습니다. 입력하신 내용을 다시 확인해주세요.'
            return render(request, 'user/login.html', context)


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

def mypage(request) :
    print(">>>> mypage")
    if request.session.get('member_name') :

        id = request.session.get('member_id')
        print('>>> our member', id)
        user = WebMember.objects.get(member_id=id)
        cand1posts = Post.objects.filter(writer_id=id, candidate_num=1).order_by('detail_num')
        cand2posts = Post.objects.filter(writer_id=id, candidate_num=2).order_by('detail_num')
        cand3posts = Post.objects.filter(writer_id=id, candidate_num=3).order_by('detail_num')

        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
            'user' : user,
            'cand1posts' : cand1posts,
            'cand2posts' : cand2posts,
            'cand3posts' : cand3posts,
        }
        return render(request, 'user/mypage.html', context)

def update_page(request):
    print('>>> update_page')

    context = {
        'session_member_name': request.session.get('member_name'),
        'session_member_id': request.session.get('member_id'),
    }
    return render(request, 'user/member_update.html', context)

def update(request):
    print('>>>> user update ')

    id = request.POST['id']
    pwd = request.POST['pwd']
    name = request.POST['name']
    poli = request.POST['poli']
    age = request.POST['age']
    print('>>>> param values - ', id, pwd, name, poli, age)

    # orm - update
    member = WebMember.objects.get(member_id=id)
    member.member_pwd = pwd
    member.member_name = name
    member.member_poli = poli
    member.member_age = age
    member.save()

    print(member)

    return redirect('mypage')

def remove(request):
    print('>>> remove')

    id= request.session.get('member_id')
    member = WebMember.objects.get(member_id=id)
    member.delete()
    request.session['member_name'] = {}
    request.session['member_id'] = {}
    request.session.modified = True

    return redirect('../../whovo')