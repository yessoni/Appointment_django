from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import calendar
from django.db.models import Sum

# Create your views here.


@login_required(login_url='/login')
def Dashboard(request):
    return render(request, 'registration/index.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {username}.")
            return redirect("home")
        else:
            messages.error(request, "Invalid email or password.")
    form = UserLoginForm()
    return render(request=request, template_name="registration/login.html", context={"login_form": form})

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
            new_product.enterd_by = request.user.first_name
            new_product.save()
            return redirect('home')
    else:
        form = AddProductForm()
    return render(request, 'registration/add_product.html', {'form': form})


@login_required(login_url='/login')
def all_product(request):
    if request.method == 'GET':
        product = AddProduct.objects.all()
    return render(request, 'registration/all_products.html', {'product': product})


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login')
def add_doctor(request):
    if request.method == 'POST':
        form = AddDoctorForm(data=request.POST)
        if form.is_valid():
            new_doctor = form.save(commit=False)
            new_doctor.enterd_by = request.user.first_name
            new_doctor.save()
            return redirect('add_doctor')
    else:
        form = AddDoctorForm()
    return render(request, 'registration/add_doctor.html', {'form': form})


@login_required(login_url='/login')
def all_doctor(request):
    if request.method == 'GET':
        doctor = AddDoctor.objects.all()
        return render(request, 'registration/schedule_doctor_appointment.html', {'doctor': doctor})

    if request.method == 'POST':
        doctor_name = request.POST['doctor-name']
        appointment_date = request.POST['datepicker']
        appointment_time = request.POST['datetime']
        paitent_appointment = DoctorAppointment.objects.create(doctor_name=doctor_name, date_appointment=appointment_date,
                                                               time_appointment=appointment_time, enterd_by=request.user.first_name)
        paitent_appointment.save()
        return redirect('doctor')


@login_required(login_url='/login')
def today_date_schedule(request):
    if request.method == 'GET':
        return render(request, 'registration/today_schedule_details.html')

    if request.method == 'POST':
        today_date = request.POST['datepicker']
        today_date_data = DoctorAppointment.objects.filter(
            date_appointment=today_date)
        return render(request, 'registration/particular_day_schedule.html', {'today_date_data': today_date_data})


@login_required(login_url='/login')
def deals_details(request):
    if request.method == 'GET':
        doctor = AddDoctor.objects.all()
        return render(request, 'registration/deals_detail.html', {'doctor': doctor})

    if request.method == 'POST':
        doctor_name = request.POST['doctor-name']
        product_name = request.POST['product_name']
        quantity_order = request.POST['quantity_order']
        new_deal_data = DealsDetails.objects.create(
            doctor_name=doctor_name, product_name=product_name, quantity_ordered=quantity_order, enterd_by=request.user.first_name)
        new_deal_data.save()
        return redirect('deals_details')


@login_required(login_url='/login')
def list_of_employee(request):
    created_by_admin = User.objects.all().exclude(is_superuser=True)
    return render(request, 'registration/list_of_employee.html', {'employee': created_by_admin})


@login_required(login_url='/login')
def product_by_employee(request):
    employee_name = User.objects.all().exclude(is_superuser=True)
    employee = request.POST.get('product_data', False)
    owner_product = AddProduct.objects.filter(enterd_by=employee)
    return render(request, 'registration/owner_product.html', {'employee_name': employee_name, 'owner_product': owner_product})


def deals_with_employee(request):
    if request.method == 'GET':
        employee_deals = User.objects.all().exclude(is_superuser=True)
        monthly = {name: num for num, name in enumerate(
            calendar.month_abbr) if num}
        return render(request, 'registration/deals_owner.html', {'employee_name': employee_deals, "month": monthly.keys()})

    if request.method == 'POST':
        select_month = request.POST.get('months', False)
        select_employee = request.POST.get('employee_data', False)
        employee_deals = User.objects.all().exclude(is_superuser=True)
        monthly = {name: num for num, name in enumerate(
            calendar.month_abbr) if num}
        employee = DealsDetails.objects.filter(
            enterd_by=select_employee, month__month=monthly[select_month])
        return render(request, 'registration/deals_owner.html', {'employee_name': employee_deals, "month": monthly.keys(), 'employee': employee})


def doctor_vist_detail(request):
    if request.method == 'GET':
        employee_deals = User.objects.all().exclude(is_superuser=True)
        monthly = {name: num for num, name in enumerate(
            calendar.month_abbr) if num}
        return render(request, 'registration/doctor_vist.html', {'employee_name': employee_deals, "month": monthly.keys()})

    if request.method == 'POST':
        select_month = request.POST.get('months', False)
        select_employee = request.POST.get('employee_data', False)
        employee_deals = User.objects.all().exclude(is_superuser=True)
        monthly = {name: num for num, name in enumerate(
            calendar.month_abbr) if num}
        employee = DoctorAppointment.objects.filter(
            enterd_by=select_employee, date_appointment__month=monthly[select_month]).distinct('enterd_by')
        total_month_appointment = DoctorAppointment.objects.filter(
            enterd_by=select_employee, date_appointment__month=monthly[select_month]).count()
        print('****************************',total_month_appointment)
        return render(request, 'registration/doctor_vist.html', {'employee_name': employee_deals, "month": monthly.keys(), 'employee': employee, 'appointment_count':total_month_appointment})
