from django.contrib import admin
from django.urls    import path,include
from bbsApp         import views


urlpatterns = [
    path('whovo/', views.index, name = 'bbs_whovo'),
    path('blog/',   views.blog, name='bbs_blog'),
    path('events/', views.events, name='bbs_events'),
    path('postForm/', views.postForm, name='postForm')
]
