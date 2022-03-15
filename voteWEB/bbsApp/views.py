from django.shortcuts import render, redirect
from.models           import *
from django.http      import JsonResponse
from .urls            import *


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
            'create_date': bbs.create_date,
        })

    return JsonResponse(jsonAry, safe=False)


    # return render(request, 'html' )

def remove(request):
    print('>>>> bbs remove')

    id = request.GET['id']
    print('debug - ', id)

    post = Post.objects.get(id = id)
    post.delete()

    return redirect ('candidate2_detail01')





