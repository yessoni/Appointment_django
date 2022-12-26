from django.urls import path,include
from .views import *

urlpatterns = [
    path('',Dashboard,name='home'),
    path('login/',Login,name='login'),
    path('add_product/',add_product,name='add_product'),
    path('product/',all_product,name='all_product'),
    path('logout/',logoutUser,name='logout'),
]
