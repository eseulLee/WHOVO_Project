from django.urls import path, include
from candidate2App import views

urlpatterns = [
    path('index/', views.candidate2),
]