from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,'base/home.html')

def Login(request):
    page = 'login'
    context = {"page":page}
    return render(request,'base/login.html',context)

def Signup(request):
    return render(request,'base/login.html')