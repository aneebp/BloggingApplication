from django.shortcuts import render

# Create your views here.

def Home(request):
    context = {}
    return render(request,'base/home.html',context)

def Login(request):
    page = 'login'
    context = {"page":page}
    return render(request,'base/login.html',context)

def Signup(request):
    context = {}
    return render(request,'base/login.html',context)

def Createblogge(request):
    context = {}
    return render(request,'base/blog_create_form.html',context)