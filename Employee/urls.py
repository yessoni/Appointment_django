from django.urls import path,include
from .views import *

urlpatterns = [
    path('',Dashboard,name='home'),
    path('login/',Login,name='login'),
]
