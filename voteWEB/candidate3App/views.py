from django.shortcuts import render, redirect

# Create your views here.

def candidate3(request):
    print('>>> candidate3 index')
    if request.session.get('member_name') :
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name' :  request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
        }
        return render(request, 'candidate3/candidate3.html',context)
    else:
        return render(request, 'candidate3/candidate3.html' )

def detail01(request):
    print('>>> candidate2')
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
        }
        return render(request, 'candidate3/blogDetail01.html',context)
    else:
        return render(request, 'candidate3/blogDetail01.html' )

def detail02(request):
    print('>>> detail02')
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
        }
        return render(request, 'candidate3/blogDetail02.html',context)
    else:
        return render(request, 'candidate3/blogDetail02.html' )

def detail03(request):
    print('>>> detail03')
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
        }
        return render(request, 'candidate3/blogDetail03.html',context)
    else:
        return render(request, 'candidate3/blogDetail03.html' )

def detail04(request):
    print('>>> detail04')
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
        }
        return render(request, 'candidate3/blogDetail04.html',context)
    else:
        return render(request, 'candidate3/blogDetail04.html' )

def detail05(request):
    print('>>> detail05')
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
        }
        return render(request, 'candidate3/blogDetail05.html',context)
    else:
        return render(request, 'candidate3/blogDetail05.html' )

def detail06(request):
    print('>>> detail06')
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
        }
        return render(request, 'candidate3/blogDetail06.html',context)
    else:
        return render(request, 'candidate3/blogDetail06.html' )

def detail07(request):
    print('>>> detail07')
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
        }
        return render(request, 'candidate3/blogDetail07.html',context)
    else:
        return render(request, 'candidate3/blogDetail07.html' )

def detail08(request):
    print('>>> detail08')
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
        }
        return render(request, 'candidate3/blogDetail08.html',context)
    else:
        return render(request, 'candidate3/blogDetail08.html' )

def detail09(request):
    print('>>> detail09')
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
        }
        return render(request, 'candidate3/blogDetail09.html',context)
    else:
        return render(request, 'candidate3/blogDetail09.html' )

def detail10(request):
    print('>>> detail10')
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
        }
        return render(request, 'candidate3/blogDetail10.html',context)
    else:
        return render(request, 'candidate3/blogDetail10.html' )


