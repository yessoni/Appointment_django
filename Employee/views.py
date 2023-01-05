from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def Dashboard(request):
   return render(request, 'registration/index.html')


def Login(request):
   if request.method == 'POST':
      username = request.POST.get('username')
      password =request.POST.get('password')

      user = authenticate(request, username=username, password=password)
      if user is not None:
         login(request,user)
         messages.info(request, f"You are now logged in as {username}.")
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

@login_required(login_url='/login')
def add_product(request):
   if request.method == 'POST':
      form = AddProductForm(data=request.POST, files=request.FILES)
      if form.is_valid():
         new_product = form.save(commit=False)
         new_product.enterd_by = request.user
         new_product.save()
         return redirect('home')
   else:
      form = AddProductForm()
   return render(request, 'registration/add_product.html', {'form':form})


@login_required(login_url='/login')
def all_product(request):
   if request.method == 'GET':
      product = AddProduct.objects.all()
   return render(request, 'registration/all_products.html', {'product':product})


def logoutUser(request):
	logout(request)
	return redirect('login') 


@login_required(login_url='/login')
def add_doctor(request):
   if request.method == 'POST':
      form = AddDoctorForm(data=request.POST)
      if form.is_valid():
         new_doctor = form.save(commit=False)
         new_doctor.enterd_by = request.user
         new_doctor.save()
         return redirect('add_doctor')
   else:
      form = AddDoctorForm()
   return render(request, 'registration/add_doctor.html', {'form':form})


@login_required(login_url='/login')
def all_doctor(request):
   if request.method == 'GET':
      doctor = AddDoctor.objects.all()
   return render(request, 'registration/schedule_doctor_appointment.html', {'doctor':doctor})