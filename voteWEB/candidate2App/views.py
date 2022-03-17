from django.shortcuts import render, redirect
from bbsApp.models import Post
from django.db.models import Count

# Create your views here.

def candidate2(request):
    print('>>> candidate2 index')

    candidate_num = 2

    Posts = Post.objects.filter(candidate_num=candidate_num).values('detail_num').annotate(dcount=Count('detail_num'))
    # select detal_num , count(detail_num) as dcount from table group by detail_num

    dcount1 = Posts.get(detail_num=1)['dcount']
    dcount2 = Posts.get(detail_num=2)['dcount']
    dcount3 = Posts.get(detail_num=3)['dcount']
    dcount4 = Posts.get(detail_num=4)['dcount']
    dcount5 = Posts.get(detail_num=5)['dcount']
    dcount6 = Posts.get(detail_num=6)['dcount']
    dcount7 = Posts.get(detail_num=7)['dcount']
    dcount8 = Posts.get(detail_num=8)['dcount']
    dcount9 = Posts.get(detail_num=9)['dcount']
    dcount10 = Posts.get(detail_num=10)['dcount']

    if request.session.get('member_name'):
        context = {
            'session_member_name': request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
            'candidate_num': candidate_num,
            'dcount1': dcount1, 'dcount2': dcount2, 'dcount3': dcount3, 'dcount4': dcount4, 'dcount5': dcount5,
            'dcount6': dcount6, 'dcount7': dcount7, 'dcount8': dcount8, 'dcount9': dcount9, 'dcount10': dcount10
        }

        return render(request, 'candidate2/candidate2.html', context)
    else:
        context = {
            'candidate_num': candidate_num,
            'dcount1': dcount1, 'dcount2': dcount2, 'dcount3': dcount3, 'dcount4': dcount4, 'dcount5': dcount5,
            'dcount6': dcount6, 'dcount7': dcount7, 'dcount8': dcount8, 'dcount9': dcount9, 'dcount10': dcount10
        }
        return render(request, 'candidate2/candidate2.html', context)

def detail01(request):
    print('>>> candidate2')
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
    print('>>> candidate2')
    candidate_num = 2
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
        return render(request, 'candidate2/blogDetail02.html', context)
    else:
        context = {
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate2/blogDetail02.html', context)

def detail03(request):
    print('>>> detail03')
    candidate_num = 2
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
        return render(request, 'candidate2/blogDetail03.html', context)
    else:
        context = {
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate2/blogDetail03.html', context)

def detail04(request):
    print('>>> detail04')
    candidate_num = 2
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
        return render(request, 'candidate2/blogDetail04.html', context)
    else:
        context = {
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate2/blogDetail04.html', context)

def detail05(request):
    print('>>> detail05')
    candidate_num = 2
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
        return render(request, 'candidate2/blogDetail05.html', context)
    else:
        context = {
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate2/blogDetail05.html', context)

def detail06(request):
    print('>>> detail06')
    candidate_num = 2
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
        return render(request, 'candidate2/blogDetail06.html', context)
    else:
        context = {
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate2/blogDetail06.html', context)

def detail07(request):
    print('>>> detail07')
    candidate_num = 2
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
        return render(request, 'candidate2/blogDetail07.html', context)
    else:
        context = {
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate2/blogDetail07.html', context)

def detail08(request):
    print('>>> detail08')
    candidate_num = 2
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
        return render(request, 'candidate2/blogDetail08.html', context)
    else:
        context = {
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate2/blogDetail08.html', context)

def detail09(request):
    print('>>> detail09')
    candidate_num = 2
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
        return render(request, 'candidate2/blogDetail09.html', context)
    else:
        context = {
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate2/blogDetail09.html', context)

def detail10(request):
    print('>>> detail10')
    candidate_num = 2
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
        return render(request, 'candidate2/blogDetail10.html', context)
    else:
        context = {
            'candidate_num': candidate_num,
            'detail_num': detail_num,
            'Posts': Posts
        }
        return render(request, 'candidate2/blogDetail10.html', context)


