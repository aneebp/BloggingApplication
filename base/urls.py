from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('login',views.Login,name='login'),
    path('signup',views.Signup,name='signup'),
    path('create_blogge',views.Createblogge,name='createblogge'),
    path('profile',views.Profile,name='profile'),
    path('edit_profile',views.ProfileEdit,name='profile_edit')

]