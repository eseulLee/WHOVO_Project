from django.urls import path, include
from candidate2App import views

urlpatterns = [
    path('index/', views.candidate2),
    path('detail01/', views.detail01, name='2_1'),
    path('detail02/', views.detail02),
    path('detail03/', views.detail03),
    path('detail04/', views.detail04),
    path('detail05/', views.detail05),
    path('detail06/', views.detail06),
    path('detail07/', views.detail07),
    path('detail08/', views.detail08),
    path('detail09/', views.detail09),
    path('detail10/', views.detail10),
]