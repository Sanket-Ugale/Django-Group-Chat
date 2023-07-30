from django.shortcuts import render
from .forms import SignUpForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
# Create your views here.
def frontpage(request):
    context={}
    return render(request,"frontpage.html", context)

def signup(request):
    if request.method=="POST":
        form =SignUpForm(request.POST)

        if form.is_valid():
            user=form.save()

            login(request,user)
            return redirect('frontpage')
    else:
        form=SignUpForm()
    return render(request,"signup.html",{"form":form})

def login(request):
    return render(request,"login.html")