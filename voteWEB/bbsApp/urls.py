from django.contrib import admin
from django.urls    import path,include
from bbsApp         import views


urlpatterns = [
    path('blog/',   views.blog, name='blog'),
    path('events/', views.events, name='events'),
]
