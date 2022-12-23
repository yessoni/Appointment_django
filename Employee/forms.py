from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.forms.fields import EmailField  
from django.contrib.auth.models import User

class UserLoginForm(AuthenticationForm):

    def __init__(self,*args,**kwargs):
        super(UserLoginForm,self).__init__(*args, **kwargs)

    email = EmailField(widget=forms.EmailInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Enter Email Address...', 'id': 'exampleInputEmail'}))

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