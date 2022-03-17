from django.shortcuts import render, redirect
from.models           import *
from django.http      import JsonResponse
from .urls            import *

import datetime


# Create your views here.


def blog(request) :
    return render(request, 'blog.html')

def events(request):
    return render(request, 'events.html')

def postForm(request) :
    print('>>>> bbs postForm')
    candidate_num = request.POST['candidate_num']
    detail_num = request.POST['detail_num']
    writer_id = request.POST['writer_id']
    content = request.POST['content']
    # writer_time = request.POST['create_date']
    print('>>>> debuge -', candidate_num, detail_num, writer_id, content)

    # ORM - insert
    post = Post(candidate_num=candidate_num, detail_num=detail_num, writer_id=writer_id, content=content)
    post.save()
    print('>>>> post save')

    jsonAry = []
    Posts = Post.objects.filter(candidate_num=candidate_num, detail_num=detail_num)
    print('data - ', Posts)
    for bbs in Posts:
        jsonAry.append({
            'candidate_num': bbs.candidate_num,
            'detail_num': bbs.detail_num,
            'writer_id': bbs.writer_id,
            'content': bbs.content,
            'create_date': bbs.create_date.strftime('%B %d. %Y. %I:%M %p'),
            'id' : bbs.id
        })

    return JsonResponse(jsonAry, safe=False)


    # return render(request, 'html' )

def remove(request):
    print('>>>> bbs remove')

    candidate_num = request.POST['candidate_num']
    detail_num = request.POST['detail_num']
    writer_id = request.POST['writer_id']
    content = request.POST['content']
    id = request.POST['id']
    # writer_time = request.POST['create_date']
    print('>>>> debuge -', candidate_num, detail_num, writer_id, content, id)
    print('>>>> session - ', request.session.get('member_id'))

    post = Post.objects.get(id = id)
    post.delete()
    print('>>>> post deleted')

    jsonAry = []
    Posts = Post.objects.filter(candidate_num=candidate_num, detail_num=detail_num)
    print('data - ', Posts)
    for bbs in Posts:
        jsonAry.append({
            'candidate_num': bbs.candidate_num,
            'detail_num': bbs.detail_num,
            'writer_id': bbs.writer_id,
            'content': bbs.content,
            'create_date': bbs.create_date.strftime('%B %d. %Y. %I:%M %p'),
            'id' : bbs.id
        })

    return JsonResponse(jsonAry, safe=False)


def bar_chart(request):
    label = []
    data = []

    candidate = WebMember.objects.order_by('-candidate_num')
    for post in candidate:
        label.append(post.candidate_num)
        date.append(post.detail_num)

    print(label, data)


