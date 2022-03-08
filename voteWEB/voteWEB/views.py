from django.shortcuts import render

def index(request) :
    print('>>> whovo')
    if request.session.get('member_name') :
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name' :  request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
        }
        return render(request, 'index.html',context)
    else:
        return render(request, 'index.html')
