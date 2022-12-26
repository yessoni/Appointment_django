from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.forms.fields import EmailField,CharField
from django.contrib.auth.models import User

class UserLoginForm(AuthenticationForm):

    def __init__(self,*args,**kwargs):
        super(UserLoginForm,self).__init__(*args, **kwargs)

    username = CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Enter Username...', 'id': 'exampleInputEmail'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user','placeholder': 'Password','id': 'exampleInputPassword',}))


class AddProductForm(forms.ModelForm):
    class Meta:
        model = AddProduct
        # fields = '__all__'
        exclude = ('enterd_by',)
        widgets = {
            'product_name' : forms.TextInput(attrs={'class':'form-control input-md', 'placeholder':'PRODUCT NAME'}),
            'product_company_name' : forms.TextInput(attrs={'class':'form-control input-md', 'placeholder':'PRODUCT_COMPANY_NAME'}),
            'product_image' : forms.FileInput(attrs={'class':'input-file'}),
            'product_price' : forms.NumberInput(attrs={'class':'form-control input-md', 'placeholder':'PRODUCT PRICE'}),
            # 'enterd_by' : forms.TextInput(attrs={'class':'form-control input-md', 'placeholder':'ENTERD BY'}),
        }


class AddDoctorForm(forms.ModelForm):
    class Meta:
        model = AddDoctor
        # fields = '__all__'
        exclude = ('enterd_by',)
        widgets = {
            'doctor_name' : forms.TextInput(attrs={'class':'form-control input-md', 'placeholder':'DOCTOR NAME'}),
            'doctor_specialisation' : forms.TextInput(attrs={'class':'form-control input-md', 'placeholder':'PRODUCT_COMPANY_NAME'}),
            'doctor_number' : forms.FileInput(attrs={'class':'input-file'}),
            'doctor_location' : forms.NumberInput(attrs={'class':'form-control input-md', 'placeholder':'PRODUCT PRICE'}),
            # 'enterd_by' : forms.TextInput(attrs={'class':'form-control input-md', 'placeholder':'ENTERD BY'}),
        }