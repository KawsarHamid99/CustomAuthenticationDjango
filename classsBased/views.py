from django.shortcuts import render,HttpResponse
from .forms import CusAuthForm
# Create your views here.
def home(request):
    if request.method=="POST":
        fm=CusAuthForm(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data["first_name"])
            return HttpResponse("current Response")
    else:
        fm=CusAuthForm()
    return render(request,"classBased/home.html",{"form":fm})