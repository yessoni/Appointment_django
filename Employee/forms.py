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
        specialist = (
            ('chest','Chest'),
            ('heart','Heart'),
            ('general','General'),
            ('orthopadeic','Orthopadeic'),
            )
        widgets = {
            'doctor_name' : forms.TextInput(attrs={'class':'form-control input-md', 'placeholder':'DOCTOR NAME'}),
            'doctor_specialisation' : forms.Select(choices=specialist ,attrs={'class':'form-control'}),
            'doctor_number' : forms.NumberInput(attrs={'minlength': 10, 'maxlength': 10, 'required': True, 'type': 'number', 'class':'form-control', 'placeholder':'Doctor Number'}),
            'doctor_location' : forms.TextInput(attrs={'class':'form-control input-md', 'placeholder':'Doctor Location'}),
            # 'enterd_by' : forms.TextInput(attrs={'class':'form-control input-md', 'placeholder':'ENTERD BY'}),
        }