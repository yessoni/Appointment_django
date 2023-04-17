from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(AddProduct)
admin.site.register(AddDoctor)
admin.site.register(Profile)

# admin.site.site_url = "http://127.0.0.1:8000/admin/doc/"


# class MyAdminSite(admin.AdminSite):
#     def each_context(self, request):
#         print("**************************",request)
#         context = super().each_context(request)
#         context['site_url'] = self.generate_site_url(request)
#         return context

#     def generate_site_url(self, request):
#         # Here goes your custom code for dynamic url
#         url = admin.site.site_url = "http://127.0.0.1:8000/"
#         return url

# admin_site = MyAdminSite(name='/product')

# admin.site.index_template = 'registration/index.html'
# admin.autodiscover()

# from django.http import HttpResponse

# class MyAdminSite(admin.AdminSite):

#     def get_urls(self):
#         print('***********hello')
#         from django.urls import path
#         urls = super(MyAdminSite,self).get_urls()
#         urls += [
#             path('', self.admin_view(self.my_view))
#         ]       
#         return urls

#     def my_view(self, request):
#         print('***************')
#         return HttpResponse("Hello!")

# admin_site = MyAdminSite()

# from django.contrib.admin import AdminSite
# from django.http import HttpResponse

# class MyAdminSite(AdminSite):

#      def get_urls(self):
#          from django.urls import path
#          urls = super().get_urls()
#          urls += [
#              path('my_view/', self.admin_view(self.my_view))
#          ]
#          return urls

#      def my_view(self, request):
#          return HttpResponse("Hello!")

# admin_site = MyAdminSite()