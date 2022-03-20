from django.shortcuts import render, redirect
from .models          import *
from bbsApp.models    import Post
import datetime as dt
import pandas as pd
import datetime

# Create your views here.

def loginPage(request):
    print('>>>> login page')
    return render(request, 'user/login.html')

def donate(request):
    print('>>>> 회원가입 페이지')
    return render(request, 'user/donate.html')

def login(request):
    print('>>>> user login')
    df = pd.DataFrame(list(WebMember.objects.all().values()))
    lst1 = []
    lst2 = []
    lst3 = []

    # lst1 : 30대 이하 정당 지지도 / lst2 : 4050 정당 지지도 / lst3 : 60대 이상 정당 지지도
    print(df)
    print(df.describe(include='all'))
    print(df.info())
    today = datetime.date.today()
    df['member_age'] = pd.to_datetime(df['member_age'])
    print(df['member_age'], type['member_age'])
    df['birth_year'] = df['member_age'].dt.year
    df['age'] = today.year - df['birth_year'] + 1
    df_target = df[['age', 'member_poli']]
    print(df_target)
    df_l3 = df_target.loc[(df_target['age'] < 40) & (df_target['member_poli'] == '더불어민주당')]
    df_y3 = df_target.loc[(df_target['age'] < 40) & (df_target['member_poli'] == '국민의힘')]
    df_s3 = df_target.loc[(df_target['age'] < 40) & (df_target['member_poli'] == '정의당')]
    print('>>>> 30 이하 더민', df_l3, type(df_l3))
    print('>>>> 30 이하 국힘', df_y3, type(df_y3))
    print('>>>> 30 이하 정의', df_s3, type(df_s3))
    lst1 = [len(df_l3), len(df_y3), len(df_s3)]
    print(lst1)
    df_l5 = df_target.loc[((df_target['age'] >= 40) & (df_target['age'] < 60)) & (df_target['member_poli'] == '더불어민주당')]
    df_y5 = df_target.loc[((df_target['age'] >= 40) & (df_target['age'] < 60)) & (df_target['member_poli'] == '국민의힘')]
    df_s5 = df_target.loc[((df_target['age'] >= 40) & (df_target['age'] < 60)) & (df_target['member_poli'] == '정의당')]
    print(df_l5, type(df_l5), len(df_l5))
    print(df_y5, type(df_y5), len(df_y5))
    print(df_s5, type(df_s5), len(df_s5))
    lst2 = [len(df_l5), len(df_y5), len(df_s5)]
    print(lst2)
    df_l6 = df_target.loc[(df_target['age'] >= 60) & (df_target['member_poli'] == '더불어민주당')]
    df_y6 = df_target.loc[(df_target['age'] >= 60) & (df_target['member_poli'] == '국민의힘')]
    df_s6 = df_target.loc[(df_target['age'] >= 60) & (df_target['member_poli'] == '정의당')]
    print(df_l6, type(df_l6))
    print(df_y6, type(df_y6))
    print(df_s6, type(df_s6))
    lst3 = [len(df_l6), len(df_y6), len(df_s6)]
    print(lst3)

    df_poli = df[['member_poli']]
    print(df_poli)
    df_d = df_poli.loc[df_poli['member_poli'] == '더불어민주당']
    df_g = df_poli.loc[df_poli['member_poli'] == '국민의힘']
    df_j = df_poli.loc[df_poli['member_poli'] == '정의당']
    print(len(df_d), len(df_g), len(df_j))
    lst4 = [len(df_d), len(df_g), len(df_j)]
    print(lst4)

    # df = pd.DataFrame(list(WebMember.objects.all().values()))
    df_1 = pd.DataFrame(list(Post.objects.all().values()))
    df_lc = df_1.loc[df_1['candidate_num'] == 1]
    df_yc = df_1.loc[df_1['candidate_num'] == 2]
    df_sc = df_1.loc[df_1['candidate_num'] == 3]
    print(len(df_lc), len(df_yc), len(df_sc))

    lst5 = [len(df_lc), len(df_yc), len(df_sc)]

    if request.method == 'POST':
        print('>>>> request post')
        id = request.POST['id']
        pwd = request.POST['pwd']
        print('>>>> request param - ', id, pwd)
        context = {
            'chart_data1': lst1,
            'chart_data2': lst2,
            'chart_data3': lst3,
            'chart_data4': lst4,
            'chart_data5': lst5,
        }
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
    pwd2 = request.POST['pwd2']
    name = request.POST['name']
    poli = request.POST['poli']
    age = request.POST['age']
    print('>>>> param values - ', id, pwd, pwd2, name,poli,age)
    WebMember(member_id=id, member_pwd=pwd, member_name=name, member_poli=poli,member_age=age).save()
    return redirect('loginPage')


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
        print('>>>> type check', type(user.member_age), user.member_age)

        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
            'user' : user,
            'cand1posts' : cand1posts,
            'cand2posts' : cand2posts,
            'cand3posts' : cand3posts,
        }
        return render(request, 'user/mypage.html', context)

def password_check_page(request) :
    print('>>> password_check page')

    user = WebMember.objects.get(member_id=request.session.get('member_id'))

    context = {
        'session_member_name': request.session.get('member_name'),
        'session_member_id': request.session.get('member_id'),
        'user': user,
    }
    return render(request, 'user/pw_chk_for_member_update.html', context)

def password_check(request) :
    print('>>> password_check')

    if request.method == 'POST':
        print('>>>> request post')
        id = request.session.get('member_id')
        pwd = request.POST['pwd']
        print('>>>> request param - ', id, pwd)

        try:
            user = WebMember.objects.get(member_id=id, member_pwd=pwd)
            print('>>>> user 있음!')

            context = {
                'session_member_name': request.session.get('member_name'),
                'session_member_id': request.session.get('member_id'),
            }

            return render(request, 'user/member_update.html', context)

        except Exception as e:
            print('>>>> user 없음!')

            context = {
                'session_member_name': request.session.get('member_name'),
                'session_member_id': request.session.get('member_id'),
                'error': '비밀번호를 잘못 입력했습니다. 입력하신 내용을 다시 확인해주세요.'
            }

            return render(request, 'user/pw_chk_for_member_update.html', context)



def update_page(request):
    print('>>> update_page')

    user = WebMember.objects.get(member_id = request.session.get('member_id'))

    context = {
        'session_member_name': request.session.get('member_name'),
        'session_member_id': request.session.get('member_id'),
        'user' : user,
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
    mem_posts = Post.objects.filter(writer_id=id)
    mem_posts.delete()
    print('>>>> mem_posts check', mem_posts)
    request.session['member_name'] = {}
    request.session['member_id'] = {}
    request.session.modified = True

    return redirect('../../whovo')

# 아이디 실시간 체크
from django.http      import JsonResponse

def searchData(request):
    print('>>>> 회원가입 아이디체크')
    print('>>>> request.POST', request.POST)
    id = request.POST['id_value']
    print('>>>> debuge -', id)

    jsonAry = []
    try :
        user = WebMember.objects.get(member_id=id)
        jsonAry.append({
            'msg': '이미 사용중인 아이디입니다. 다시 입력해주세요.' ,
        })
        jsonAry.append({
            'idck': 'fail',
        })
    except :
        user = None
        jsonAry.append({
            'msg' : '사용가능한 아이디입니다.' ,
        })
        jsonAry.append({
            'idck': 'ok',
        })

    return JsonResponse(jsonAry, safe=False)

