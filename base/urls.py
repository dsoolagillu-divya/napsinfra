from django.urls import path
from .views import *
urlpatterns=[
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('careers',careers,name='careers'),
    path('contact/',contact,name='contact'),
    path('services/',services,name='services'),
    path('jobs/',jobs,name='jobs'),
    ]