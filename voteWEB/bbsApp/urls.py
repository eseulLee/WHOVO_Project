from django.contrib import admin
from django.urls    import path,include
from bbsApp         import views


urlpatterns = [
    path('index/', views.index, name = 'bbs_index'),
    path('login/', views.login, name = 'bbs_login'),
    path('loginPage/', views.loginPage, name='bbs_loginPage'),
    path('joinForm/', views.joinForm, name = 'joinForm'),
    path('join/',   views.join, name='join'),
    path('logout/', views.logout, name='logout'),



]
