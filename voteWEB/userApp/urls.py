from django.urls    import path , include
from userApp        import views

urlpatterns = [
    path('index/', views.loginPage, name='loginPage'),
    path('registerForm/', views.donate, name='joinForm'),
    path('login/', views.login, name = 'bbs_login'),
    path('join/',   views.join, name='join'),
    path('logout/', views.logout, name='logout'),
]