from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.http import HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

def loginuser(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return  redirect("/")
        else:
            return render(request,"login.html")

    return render(request,"login.html")

def logoutuser(request):
    logout(request)
    return redirect("/login")


def blogs(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'blogs.html')

def contact(request):
    if request.user.is_anonymous:
        return redirect("/login")

    if request.method=="POST":
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        contact=Contact(email=email,desc=desc,date=datetime.today())
        contact.save()
    return render(request,'contact.html')