from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate,login,logout

def home(request):
    return render(request,"index.html")

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

def user_login(request):
    if request.method=='GET':
        return render(request,"login.html")
  
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            print(request.user)
            return HttpResponseRedirect("/products")
        else:
            return render(request,"login.html",{"message":"Log in failed"})
        
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/login")
        

def register(request):
    if request.method=="GET":
        form=CustomUserCreationForm()
        return render(request,"register.html",{"form":form})
    else:
        submited_form=CustomUserCreationForm(request.POST)
        if submited_form.is_valid():
            submited_form.save()
            return HttpResponseRedirect("/login")
        return render(request,"register.html    ",{"form":submited_form})

