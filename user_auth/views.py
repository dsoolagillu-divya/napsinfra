from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import logging

# Create your views here.
def login_(request):
    if request.method == 'POST':
        a = request.POST['username']
        b = request.POST['password']
        u = authenticate(username = a,password = b)
        if u:
            login(request,u)
            return redirect('home')
        else:
            return render(request,'login_.html',{'status':'username or password are invalid'})
    return render(request,'login_.html')

def register(request):
   
    if request.method=='POST':
        a=request.POST['fname']
        b=request.POST['lname']
        c=request.POST['email']
        d=request.POST['username']
        e=request.POST['password']
        logger = logging.getLogger(__name__)
        logger.info(f"{a} {b} {c} {d}")
        try:
            v= User.objects.get(username=d)
            return render(request,'register.html',{'status':'username already exists'})
        except:
            u=User.objects.create(
                first_name=a,
                last_name=b,
                email=c,
                username=d,
               
            )
            u.set_password(e)
            u.save()
           
           

            return redirect('login_')
    return render(request,'register.html')
def login_(request):
    print(request.method)
    print(request.POST)
    if request.method=='POST':
        a=request.POST['username']
        b=request.POST['password']
        print(a,b)
        u=authenticate(username=a,password=b)
        print(u)
        if u:
            login(request,u)
            return redirect('home')
        else:
            return render(request,'login_.html',{'error':'Entered wrong username or password'})
    return render(request,'login_.html')
@login_required(login_url='login_')
def profile(request):
    return render(request,'profile.html')
@login_required(login_url='login_')

@login_required(login_url='login_')
def reset_pass(request):
    if request.method == 'POST':
        if 'oldpasw' in request.POST:
            a = request.POST['oldpasw']
            auth = authenticate(username=request.user.username,password=a)
            if auth:
                return render(request,'reset_pass.html',{'new_pass':True})
            else:
                return render(request,'reset_pass.html',{'wrong':True})
        if 'newpasw' in request.POST:
            b=request.POST['newpasw']
            if request.user.check_password(b):
                return render(request,'reset_pass.html',{'same':True})
            request.user.set_password(b)
            request.user.save()
            return redirect('login_')
    return render(request,'reset_pass.html')

def logout_(request):
    logout(request)
    return redirect('login_')
def reset_password(request):
    if request.method=='POST':
        if 'oldpasw' in request.POST:
            oldpass=request.POST['oldpasw']
            print(oldpass)
            u=authenticate(username=request.user.username,password=oldpass)
            print(u)
            if u:
                return render(request,'reset_password.html')
            else:
                return render(request,'reset_password.html')
        if 'newpasw' in request.POST:
            newpass=request.POST['newpasw']
            print(newpass)
            if request.user.check_password(newpass):
                return render(request,'reset_password.html')
            request.user.set_password(newpass)
            request.user.save()
            return redirect('login')
        return render(request,'reset_password.html')
def forgot_password(request):
    if request.method=='POST':
        username=request.POST['username']
        print(username)
        try:
            u=User.objects.get(username=username)
            request.session['fp_user']=u.username
            print(u)
        except:
            return render(request,'forgot_password.html',{'error':'username does not exist'})
    return render(request,'forgot_password.html')
def new_password(request):
    username=request.session.get('fp_user')
    if username is None:
        return redirect('forget_pass')
    user=User.objects.get(username=username)
    if request.method =='POST':
        new=request.POST['password']
        if user.check_password(new):
            return render(request,'new_password.html',{'error':True})
        user.set_password(new)
        user.save()
        del request.session['fp_user']
        return redirect('login')
        




