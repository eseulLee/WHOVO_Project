from django.contrib import admin
from django.urls    import path,include
from bbsApp         import views


urlpatterns = [
    path('blog/',   views.blog, name='bbs_blog'),
    path('events/', views.events, name='bbs_events'),
    path('postForm/', views.postForm, name='postForm'),
    path('remove/', views.remove, name='remove'),

]
