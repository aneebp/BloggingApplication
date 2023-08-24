from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate ,login,logout
from .models import User,Blogge,Comment
from django.contrib import messages

# Create your views here.

def Home(request):
    context = {}
    return render(request,'base/home.html',context)

def Login(request):
    page = 'login'
    # if request.user.is_authenticated:
    #     return redirect('home')
    if request.method == 'POST':
        username = request.POST.get("username").lower()
        password = request.POST.get("password")
        # try:
        #     user = User.objects.get(username=username)
        # except:
        #     messages.error(request,'User does not exit ')
        user = authenticate(request , username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'username or password does not exist')   
             
    context = {"page":page}
    return render(request,'base/login.html',context)

def Signup(request):
    context = {}
    return render(request,'base/login.html',context)

def Createblogge(request):
    context = {}
    return render(request,'base/blog_create_form.html',context)

def Profile(request):
    context ={}
    return render(request,'base/user_profile.html',context)

def ProfileEdit(request):
    context ={}
    return render(request,'base/profile_edit.html',context)