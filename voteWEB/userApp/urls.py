from django.urls    import path , include
from userApp        import views

urlpatterns = [
    path('index/', views.loginPage, name='loginPage'),
    path('registerForm/', views.donate, name='joinForm'),
    path('login/', views.login, name = 'bbs_login'),
    path('join/',   views.join, name='join'),
    path('logout/', views.logout, name='logout'),
    path('change/', views.mypage, name='change'),
    path('mypage/', views.mypage, name='mypage'),
    path('update_page/', views.update_page, name='update_page'),
    path('update/', views.update, name='update'),
    path('remove/', views.remove, name='remove'),
    path('searchData/', views.searchData, name='searchData'),
    path('password_check_page/', views.password_check_page, name='password_check_page'),
    path('password_check/', views.password_check, name='password_check'),

]