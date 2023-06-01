from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .forms import UserAuthenticationForm,MyUserCreationForm,MyUserChangeDetailsForm
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from .forms import MyUSersetPasswordForm,MyUserChangePasswordForm
from django.contrib import messages
# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm=UserAuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                name=fm.cleaned_data["username"]
                password=fm.cleaned_data['password']
                user=authenticate(username=name,password=password)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect("/")

            return render(request,"funcbased/signin.html",{"form":fm})
        else:
            fm=UserAuthenticationForm()
            return render(request,"funcbased/signin.html",{"form":fm})
    else:
        return HttpResponseRedirect("/details/")
    
def signupForm(request):
    if request.method=="POST":
        fm=MyUserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponse("User REGISTRATION  completed")
        return HttpResponseRedirect("/")
    else:
        fm=MyUserCreationForm()
        return render(request,"funcbased/Authen.html",{'form':fm,'type':"signup"})

        
def details(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=MyUserChangeDetailsForm(request.POST,instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request,"user updated successfully...")
                return HttpResponseRedirect("/details/")
        else:
            fm=MyUserChangeDetailsForm(instance=request.user)
        return render(request,"funcbased/Authen.html",{'form':fm,"type":"User Details"})
    
    else:
        return HttpResponseRedirect("/")
        
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")


def setuserpassword(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=MyUSersetPasswordForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,"Password set successfully")
                return HttpResponseRedirect("/details/")
        else:
            fm=MyUSersetPasswordForm(user=request.user)
        return render(request,"funcbased/Authen.html",{'form':fm,"type":'Set Password '})
            

    else:
        return HttpResponseRedirect("/")

def changeuserpassword(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=MyUserChangePasswordForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,"password updated successfully...")
                update_session_auth_hash(request,fm.user)
                return HttpResponseRedirect("/details/")
        else:
            fm=MyUserChangePasswordForm(user=request.user)
            return render(request,"funcbased/Authen.html",{'form':fm,"type":'Change Password '})
    else:
        return HttpResponseRedirect("/")
    