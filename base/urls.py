from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('login',views.Login,name='login'),
    path('signup',views.Signup,name='signup'),
    path('logout',views.Logout,name='logout'),
    path('create_blogge',views.Createblogge,name='createblogge'),
    path('updateblogge/<int:pk>',views.Updateblogge,name='updateblogge'),
    path('deleteblogge/<int:pk>',views.Deleteblogge,name='deleteblogge'),
    path('profile/<int:pk>',views.Profile,name='profile'),
    path('edit_profile',views.ProfileEdit,name='profile_edit')

]