from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('login',views.Login,name='login'),
    path('signup',views.Signup,name='signup')
]