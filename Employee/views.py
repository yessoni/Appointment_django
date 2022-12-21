from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

# @login_required(login_url='login') #redirect when user is not logged in
def Dashboard(request):
   return render(request, 'registration/index.html')


def Login(request):
   if request.method == 'POST':
      email = request.POST.get('email')
      password =request.POST.get('password')

      user = authenticate(request, username=email, password=password)
      if user is not None:
         login(request,user)
         messages.info(request, f"You are now logged in as {email}.")
         return redirect("home")
      else:
         messages.error(request,"Invalid email or password.")
   form = UserLoginForm()
   return render(request=request, template_name="registration/login.html", context={"login_form":form})

   # if request.user.is_authenticated:
   #      return redirect('home')
   # else:
   #    if request.method == 'POST':
   #       email = request.POST.get('email')
   #       password =request.POST.get('password')

   #       user = authenticate(request, username=email, password=password)
   #       if user is not None:
   #          login(request,user)
   #          messages.info(request, f"You are now logged in as {email}.")
   #          return redirect("home")
   #       else:
   #          messages.error(request,"Invalid email or password.")
   #    form = UserLoginForm()
   #    return render(request=request, template_name="registration/login.html", context={"login_form":form})