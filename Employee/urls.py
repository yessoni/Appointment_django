from django.urls import path,include
from .views import *

urlpatterns = [
    path('',Dashboard,name='home'),
    path('login/',Login,name='login'),
    path('add_product/',add_product,name='add_product'),
    path('product/',all_product,name='all_product'),
    path('logout/',logoutUser,name='logout'),
    path('add_doctor/',add_doctor,name='add_doctor'),
    path('doctor/',all_doctor,name='doctor'),
    path('today-date-data/',today_date_schedule,name='today-date-data'),
    path('deals-details/',deals_details,name='deals_details'),
]
