from django.urls import path, include
from candidate3App import views

urlpatterns = [
    path('index/', views.candidate3),

]