from django.shortcuts import render
from bbsApp.models import Post
from userApp.models import WebMember

def index(request) :
    print('>>> whovo')
    if request.session.get('member_name') :
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        lst = []



        context = {
            'session_member_name' :  request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
            'chart_data' : lst
        }
        return render(request, 'index.html',context)
    else:
        return render(request, 'index.html')



