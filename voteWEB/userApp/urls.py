from django.urls    import path , include
from userApp        import views

urlpatterns = [
    path('index/', views.loginPage, name='loginPage'),
    path('registerForm', views.donate, name='joinForm'),

]