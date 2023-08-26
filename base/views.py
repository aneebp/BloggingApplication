from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate ,login,logout
from .models import User,Blogge,Comment
from django.contrib import messages
from .form import SignUpCreation

# Create your views here.

def Home(request):
    user= User.objects.all()
    context = {'user':user}
    return render(request,'base/home.html',context)

def Login(request):
    page = 'login'
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
    form = SignUpCreation()
    if request.method == "POST":
        form =SignUpCreation(request.POST)
        if form.is_valid():
            user =form.save(commit=False)
            user.username = request.POST.get("username").lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, "An error occured during registration")
    context = {'form':form}
    return render(request,'base/login.html',context)

def Logout(request):
    logout(request)
    return redirect('home')

def Createblogge(request):
    context = {}
    return render(request,'base/blog_create_form.html',context)

def Profile(request):
    context ={'user':User}
    return render(request,'base/user_profile.html',context)

def ProfileEdit(request):
    context ={}
    return render(request,'base/profile_edit.html',context)