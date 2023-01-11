from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

specialist = (
    ('chest', 'Chest'),
    ('heart', 'Heart'),
    ('general', 'General'),
    ('orthopadeic', 'Orthopadeic'),
)


class AddProduct(models.Model):
    product_name = models.CharField(max_length=255)
    product_company_name = models.CharField(max_length=255)
    product_image = models.ImageField(upload_to='images')
    product_price = models.IntegerField()
    enterd_by = models.CharField(max_length=255)


class AddDoctor(models.Model):
    doctor_name = models.CharField(max_length=255)
    doctor_specialisation = models.CharField(
        max_length=50, choices=specialist, default='general')
    doctor_number = models.IntegerField()
    doctor_location = models.CharField(max_length=50)
    enterd_by = models.CharField(max_length=255)


class DoctorAppointment(models.Model):
    doctor_name = models.CharField(max_length=255)
    date_appointment = models.DateField()
    time_appointment = models.TimeField()
    enterd_by = models.CharField(max_length=255)


class DealsDetails(models.Model):
    doctor_name = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    quantity_ordered = models.IntegerField()
    month = models.DateField(auto_now=True)
    enterd_by = models.CharField(max_length=255)


from django.db.models.signals import post_save
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def create_user_profile(sender, instance, created, **kwargs):  
        if created:  
            profile, created = Profile.objects.get_or_create(user=instance)  

    post_save.connect(create_user_profile, sender=User) 



from django.conf import settings
class LoggedInUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='logged_in_user', on_delete=models.CASCADE)
    session_key = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.user.username