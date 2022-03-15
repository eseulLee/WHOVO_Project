from django.shortcuts import render, redirect
from bbsApp.models import Post

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
    print('>>> candidate2')
    candidate_num = 1
    detail_num = 1

    Posts = Post.objects.filter(candidate_num=candidate_num, detail_num=detail_num)
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate1/blogDetail1.html', context)
    else:
        context = {
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate1/blogDetail1.html', context)

def detail02(request):
    print('>>> candidate2')
    candidate_num = 1
    detail_num = 2

    Posts = Post.objects.filter(candidate_num=candidate_num, detail_num=detail_num)
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate1/blogDetail2.html', context)
    else:
        context = {
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate1/blogDetail2.html', context)

def detail03(request):
    print('>>> candidate2')
    candidate_num = 1
    detail_num = 3

    Posts = Post.objects.filter(candidate_num=candidate_num, detail_num=detail_num)
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate1/blogDetail3.html', context)
    else:
        context = {
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate1/blogDetail3.html', context)

def detail04(request):
    print('>>> candidate2')
    candidate_num = 1
    detail_num = 4

    Posts = Post.objects.filter(candidate_num=candidate_num, detail_num=detail_num)
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate1/blogDetail4.html', context)
    else:
        context = {
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate1/blogDetail4.html', context)

def detail05(request):
    print('>>> candidate2')
    candidate_num = 1
    detail_num = 5

    Posts = Post.objects.filter(candidate_num=candidate_num, detail_num=detail_num)
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate1/blogDetail5.html', context)
    else:
        context = {
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate1/blogDetail5.html', context)

def detail06(request):
    print('>>> candidate2')
    candidate_num = 1
    detail_num = 6

    Posts = Post.objects.filter(candidate_num=candidate_num, detail_num=detail_num)
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate1/blogDetail6.html', context)
    else:
        context = {
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate1/blogDetail6.html', context)

def detail07(request):
    print('>>> candidate2')
    candidate_num = 1
    detail_num = 7

    Posts = Post.objects.filter(candidate_num=candidate_num, detail_num=detail_num)
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate1/blogDetail7.html', context)
    else:
        context = {
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate1/blogDetail7.html', context)

def detail08(request):
    print('>>> candidate2')
    candidate_num = 1
    detail_num = 8

    Posts = Post.objects.filter(candidate_num=candidate_num, detail_num=detail_num)
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate1/blogDetail8.html', context)
    else:
        context = {
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate1/blogDetail8.html', context)

def detail09(request):
    print('>>> candidate1')
    candidate_num = 1
    detail_num = 9

    Posts = Post.objects.filter(candidate_num=candidate_num, detail_num=detail_num)
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate1/blogDetail9.html', context)
    else:
        context = {
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate1/blogDetail9.html', context)

def detail10(request):
    print('>>> candidate2')
    candidate_num = 1
    detail_num = 10

    Posts = Post.objects.filter(candidate_num=candidate_num, detail_num=detail_num)
    if request.session.get('member_name'):
        print('>>> our member')
        # 세션을 계속 심어줘야 함
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate1/blogDetail10.html', context)
    else:
        context = {
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate1/blogDetail10.html', context)
