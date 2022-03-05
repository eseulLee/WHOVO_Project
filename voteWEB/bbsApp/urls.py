from django.contrib import admin
from django.urls    import path,include
from bbsApp         import views


urlpatterns = [
    path('whovo/', views.index, name = 'whovo'),
    path('login/', views.login, name = 'bbs_login'),
    path('loginPage/', views.loginPage, name='bbs_loginPage'),
    path('joinForm/', views.joinForm, name = 'joinForm'),
    path('join/',   views.join, name='join'),
    path('logout/', views.logout, name='logout'),
    path('blog/',   views.blog, name='blog'),
    path('candidate1/', views.candidate1, name='candidate1'),
    path('candidate2/', views.candidate2, name='candidate2'),
    path('candidate3/', views.candidate3, name='candidate3'),
    path('blog-two-details/', views.blogDetail, name='blog_detail'),
    path('donate/', views.donate, name='donate'),
    path('donate/', views.donate, name='donate'),
    path('events/', views.events, name='events'),
]
