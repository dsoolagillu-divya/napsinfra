from django.urls import path
from .views import *
urlpatterns=[
    path('',register,name='register'),
   path('login_',login_,name='login_'),
    path('profile/',profile,name='profile'),
    path('logout_',logout_,name='logout_'),
    path('reset_password/',reset_password,name='reset_password'),
    path('forgot_password/',forgot_password,name='forgot_password')
    

]