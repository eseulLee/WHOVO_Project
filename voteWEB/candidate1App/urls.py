from django.urls    import path , include
from candidate1App        import views

urlpatterns = [
    path('index/', views.candidate1),
    path('datail01/', views.detail01),


]
