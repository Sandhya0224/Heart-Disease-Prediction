from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('prediction/', views.prediction, name='prediction'),
    path('login/', views.userlogin, name='login'),
    path('registration/', views.registration, name='registration'),
    path('logout/',views.userlogout,name='logout')
]