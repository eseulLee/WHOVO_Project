from django.shortcuts import render
from bbsApp.models import Post
from userApp.models import WebMember
import datetime

def index(request) :
    print('>>> whovo')
    # lst1 : 30대 이하 정당 지지도 / lst2 : 4050 정당 지지도 / lst3 : 60대 이상 정당 지지도
    lst1 = []
    lst2 = []
    lst3 = []

    # users_age = WebMember.objects.values('member_age')
    # users_poli = WebMember.objects.values('member_poli')
    # print(users_age)

    # for user in users:
    #     birth_year = user['member_age'].year
    #     today_year = datetime.date.today().year
    #     mem_age = today_year - birth_year + 1
    #     if mem_age <= 39:
    #
    #         lst1.append(mem_age)
    #     elif mem_age <= 59:
    #         lst2.append(mem_age)
    #     else:
    #         lst3.append(mem_age)
    # 선호정당 별 user 구분 (4)
    cand1_users = WebMember.objects.filter(member_poli = '더불어민주당')
    cand2_users = WebMember.objects.filter(member_poli = '국민의힘')
    cand3_users = WebMember.objects.filter(member_poli = '정의당')
    for user in cand1_users :
        # birth = user.values('member_age')
        # print(user.objects.values('member_age'))
        pass
    print('>>>> 데이터가 모였다', lst1, lst2, lst3)







    if request.session.get('member_name') :
        print('>>> our member')
        # 세션을 계속 심어줘야 함

        context = {
            'session_member_name' :  request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
            'chart_data1' : lst1,
            'chart_data2': lst2,
            'chart_data3': lst3,

        }
        return render(request, 'index.html',context)
    else:
        context = {
            'chart_data1': lst1,
            'chart_data2': lst2,
            'chart_data3': lst3,
        }

        return render(request, 'index.html', context)



