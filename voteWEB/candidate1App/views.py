from django.shortcuts import render, redirect

# Create your views here.

def candidate1(request):
    print('>>> candidate1 index')
    if request.session.get('member_name') :
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name' :  request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
        }
        return render(request, 'candidate1/candidate1.html',context)
    else:
        return render(request, 'candidate1/candidate1.html' )

def detail01(request):
    print('>>> candidate1')
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
        }
        return render(request, 'candidate1/blogDetail1.html',context)
    else:
        return render(request, 'candidate1/blogDetail1.html' )

def detail02(request):
    print('>>> detail02')
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
        }
        return render(request, 'candidate1/blogDetail2.html',context)
    else:
        return render(request, 'candidate1/blogDetail2.html' )

def detail03(request):
    print('>>> detail03')
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
        }
        return render(request, 'candidate1/blogDetail3.html',context)
    else:
        return render(request, 'candidate1/blogDetail3.html' )

def detail04(request):
    print('>>> detail04')
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
        }
        return render(request, 'candidate1/blogDetail4.html',context)
    else:
        return render(request, 'candidate1/blogDetail4.html' )

def detail05(request):
    print('>>> detail05')
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
        }
        return render(request, 'candidate1/blogDetail5.html',context)
    else:
        return render(request, 'candidate1/blogDetail5.html' )

def detail06(request):
    print('>>> detail06')
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
        }
        return render(request, 'candidate1/blogDetail6.html',context)
    else:
        return render(request, 'candidate1/blogDetail6.html' )

def detail07(request):
    print('>>> detail07')
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
        }
        return render(request, 'candidate1/blogDetail7.html',context)
    else:
        return render(request, 'candidate1/blogDetail7.html' )

def detail08(request):
    print('>>> detail08')
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
        }
        return render(request, 'candidate1/blogDetail8.html',context)
    else:
        return render(request, 'candidate1/blogDetail8.html' )

def detail09(request):
    print('>>> detail09')
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
        }
        return render(request, 'candidate1/blogDetail9.html',context)
    else:
        return render(request, 'candidate1/blogDetail9.html' )

def detail10(request):
    print('>>> detail10')
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
        }
        return render(request, 'candidate1/blogDetail10.html',context)
    else:
        return render(request, 'candidate1/blogDetail10.html' )
