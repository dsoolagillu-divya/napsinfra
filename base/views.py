from django.shortcuts import render
from django.shortcuts import render
from .models import JobApplication

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')

def careers(request):
    return render(request, 'careers.html')

    
def contact(request):
    return render(request,'contact.html')
def services(request):
    return render(request,'services.html')
def jobs(request):
    return render(request,'jobs.html')