from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    #return HttpResponse('<h1>Welcome to Upark login</h1>')
    return render (request, 'login.html')

def admin(request):
    return render (request, 'admin.html')

def user(request):
    return render (request, 'user.html')

def visitor(request):
   return render (request, 'visitor.html')

def vehicles(request):
   return render (request, 'vehicles.html')