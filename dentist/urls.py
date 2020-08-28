from django.contrib import admin
from django.urls import path
from dentist import views

admin.site.site_header = "Login to Dentist App"
admin.site.site_title = "Welcome to Dentist's Dashboard"
admin.site.index_title = "Welcome folk"

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('blog_details', views.blog_details, name='blog_details'),
    path('contact', views.contact, name='contact'),
    path('index', views.index, name='index'),
    path('pricing', views.pricing, name='pricing'),
    path('service', views.service, name='service'),
    path('retrieveInf', views.retrieveInf, name='retrieveInf'),
]
