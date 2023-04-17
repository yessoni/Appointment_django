from django.urls import path,include
from .views import *

urlpatterns = [
    path('',Dashboard,name='home'),
    path('login/',Login,name='login'),
    path('logout/',logout_view,name='logout'),
    path('forget-password/',forget_password,name='forget-pasword'),
    path('change_password/<token>/',change_password,name='change_password'),
    path('add_product/',add_product,name='add_product'),
    path('product/',all_product,name='all_product'),
    path('logout/',logoutUser,name='logout'),
    path('add_doctor/',add_doctor,name='add_doctor'),
    path('doctor/',all_doctor,name='doctor'),
    path('today-date-data/',today_date_schedule,name='today-date-data'),
    path('deals-details/',deals_details,name='deals_details'),
    path('list_of_employee/',list_of_employee,name='list_of_employee'),
    path('employee_product/',product_by_employee,name='employee_product'),
    path('deals_owner/',deals_with_employee,name='deals_owner'),
    path('doctor_vist/',doctor_vist_detail,name='doctor_vist'),
    # path('count/',count_user),
]
