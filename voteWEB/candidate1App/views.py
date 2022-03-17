from django.shortcuts import render, redirect
from bbsApp.models import Post
from django.db.models import Count

# Create your views here.

def candidate1(request):
    print('>>> candidate1 index')

    candidate_num = 1

    Posts = Post.objects.filter(candidate_num=candidate_num).values('detail_num').annotate(dcount=Count('detail_num'))
    # select detal_num , count(detail_num) as dcount from table group by detail_num

    try:
        dcount1 = Posts.get(detail_num=1)['dcount']
    except:
        dcount1 = 0
    try:
        dcount2 = Posts.get(detail_num=2)['dcount']
    except:
        dcount2 = 0
    try:
        dcount3 = Posts.get(detail_num=3)['dcount']
    except:
        dcount3 = 0
    try:
        dcount4 = Posts.get(detail_num=4)['dcount']
    except:
        dcount4 = 0
    try:
        dcount5 = Posts.get(detail_num=5)['dcount']
    except:
        dcount5 = 0
    try:
        dcount6 = Posts.get(detail_num=6)['dcount']
    except:
        dcount6 = 0
    try:
        dcount7 = Posts.get(detail_num=7)['dcount']
    except:
        dcount7 = 0
    try:
        dcount8 = Posts.get(detail_num=8)['dcount']
    except:
        dcount8 = 0
    try:
        dcount9 = Posts.get(detail_num=9)['dcount']
    except:
        dcount9 = 0
    try:
        dcount10 = Posts.get(detail_num=10)['dcount']
    except:
        dcount10 = 0

    if request.session.get('member_name'):
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
            'candidate_num': candidate_num,
            'dcount1': dcount1, 'dcount2': dcount2, 'dcount3': dcount3, 'dcount4': dcount4, 'dcount5': dcount5,
            'dcount6': dcount6, 'dcount7': dcount7, 'dcount8': dcount8, 'dcount9': dcount9, 'dcount10': dcount10
        }

        return render(request, 'candidate1/candidate1.html', context)
    else:
        context = {
            'candidate_num': candidate_num,
            'dcount1': dcount1, 'dcount2': dcount2, 'dcount3': dcount3, 'dcount4': dcount4, 'dcount5': dcount5,
            'dcount6': dcount6, 'dcount7': dcount7, 'dcount8': dcount8, 'dcount9': dcount9, 'dcount10': dcount10
        }
        return render(request, 'candidate1/candidate1.html', context)


def detail01(request):
    print('>>> detail1')
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
    print('>>> detail2')
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
    print('>>> detail3')
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
    print('>>> detail04')
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
    print('>>> detail05')
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
    print('>>> detail06')
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
    print('>>> detail07')
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
    print('>>> detail08')
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
    print('>>> detail09')
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
    print('>>> detail10')
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
