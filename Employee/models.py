from django.db import models
from django.contrib.auth.models import User

# Create your models here.

specialist = (
    ('chest','Chest'),
    ('heart','Heart'),
    ('general','General'),
    ('orthopadeic','Orthopadeic'),
    )

class AddProduct(models.Model):
    product_name = models.CharField(max_length=255)
    product_company_name = models.CharField(max_length=255)
    product_image = models.ImageField(upload_to='images')
    product_price = models.IntegerField()
    enterd_by = models.ForeignKey(User,on_delete=models.CASCADE,)


class AddDoctor(models.Model):
    doctor_name = models.CharField(max_length=255)
    doctor_specialisation = models.CharField(max_length=50, choices=specialist, default='general')
    doctor_number = models.IntegerField()
    doctor_location = models.CharField(max_length=50)
    enterd_by = models.ForeignKey(User,on_delete=models.CASCADE,)
