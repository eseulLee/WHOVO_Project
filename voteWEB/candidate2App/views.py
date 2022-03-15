from django.shortcuts import render, redirect
from bbsApp.models import Post

# Create your views here.

def candidate2(request):
    print('>>> candidate2 index')
    if request.session.get('member_name') :
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name' :  request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
        }
        return render(request, 'candidate2/candidate2.html',context)
    else:
        return render(request, 'candidate2/candidate2.html' )

def detail01(request):
    print('>>> candidate2 detail01')
    candidate_num = 2
    detail_num = 1

    Posts = Post.objects.filter(candidate_num=candidate_num, detail_num=detail_num)
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id'  : request.session.get('member_id'),
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts' : Posts
        }
        return render(request, 'candidate2/blogDetail01.html',context)
    else:
        context = {
            'candidate_num'      : candidate_num,
            'detail_num'         : detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate2/blogDetail01.html' ,context)



def detail02(request):
    print('>>> candidate2 detail02')
    candidate_num = 2
    detail_num = 2

    Posts = Post.objects.filter(candidate_num=candidate_num, detail_num=detail_num)
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id'  : request.session.get('member_id'),
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts' : Posts
        }
        return render(request, 'candidate2/blogDetail02.html',context)
    else:
        context = {
            'candidate_num'      : candidate_num,
            'detail_num'         : detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate2/blogDetail02.html' ,context)

def detail03(request):
    print('>>> candidate2 detail03')
    candidate_num = 2
    detail_num = 3

    Posts = Post.objects.filter(candidate_num=candidate_num, detail_num=detail_num)
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id'  : request.session.get('member_id'),
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts' : Posts
        }
        return render(request, 'candidate2/blogDetail03.html',context)
    else:
        context = {
            'candidate_num'      : candidate_num,
            'detail_num'         : detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate2/blogDetail03.html' ,context)

def detail04(request):
    print('>>> candidate2 detail04')
    candidate_num = 2
    detail_num = 4

    Posts = Post.objects.filter(candidate_num=candidate_num, detail_num=detail_num)
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id'  : request.session.get('member_id'),
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts' : Posts
        }
        return render(request, 'candidate2/blogDetail04.html',context)
    else:
        context = {
            'candidate_num'      : candidate_num,
            'detail_num'         : detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate2/blogDetail04.html' ,context)

def detail05(request):
    print('>>> candidate2 detail05')
    candidate_num = 2
    detail_num = 5

    Posts = Post.objects.filter(candidate_num=candidate_num, detail_num=detail_num)
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id'  : request.session.get('member_id'),
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts' : Posts
        }
        return render(request, 'candidate2/blogDetail05.html',context)
    else:
        context = {
            'candidate_num'      : candidate_num,
            'detail_num'         : detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate2/blogDetail05.html' ,context)

def detail06(request):
    print('>>> candidate2 detail06')
    candidate_num = 2
    detail_num = 6

    Posts = Post.objects.filter(candidate_num=candidate_num, detail_num=detail_num)
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id'  : request.session.get('member_id'),
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts' : Posts
        }
        return render(request, 'candidate2/blogDetail06.html',context)
    else:
        context = {
            'candidate_num'      : candidate_num,
            'detail_num'         : detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate2/blogDetail06.html' ,context)

def detail07(request):
    print('>>> candidate2 detail07')
    candidate_num = 2
    detail_num = 7

    Posts = Post.objects.filter(candidate_num=candidate_num, detail_num=detail_num)
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id'  : request.session.get('member_id'),
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts' : Posts
        }
        return render(request, 'candidate2/blogDetail07.html',context)
    else:
        context = {
            'candidate_num'      : candidate_num,
            'detail_num'         : detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate2/blogDetail07.html' ,context)

def detail08(request):
    print('>>> candidate2 detail08')
    candidate_num = 2
    detail_num = 8

    Posts = Post.objects.filter(candidate_num=candidate_num, detail_num=detail_num)
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id'  : request.session.get('member_id'),
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts' : Posts
        }
        return render(request, 'candidate2/blogDetail08.html',context)
    else:
        context = {
            'candidate_num'      : candidate_num,
            'detail_num'         : detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate2/blogDetail08.html' ,context)

def detail09(request):
    print('>>> candidate2 detail09')
    candidate_num = 2
    detail_num = 9

    Posts = Post.objects.filter(candidate_num=candidate_num, detail_num=detail_num)
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id'  : request.session.get('member_id'),
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts' : Posts
        }
        return render(request, 'candidate2/blogDetail09.html',context)
    else:
        context = {
            'candidate_num'      : candidate_num,
            'detail_num'         : detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate2/blogDetail09.html' ,context)

def detail10(request):
    print('>>> candidate2 detail10')
    candidate_num = 2
    detail_num = 10

    Posts = Post.objects.filter(candidate_num=candidate_num, detail_num=detail_num)
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id'  : request.session.get('member_id'),
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts' : Posts
        }
        return render(request, 'candidate2/blogDetail10.html',context)
    else:
        context = {
            'candidate_num'      : candidate_num,
            'detail_num'         : detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate2/blogDetail10.html' ,context)


