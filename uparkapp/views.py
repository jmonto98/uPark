from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from .models import *
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

def vehicle(request):
    vehiclelist=Vehicle.objects.all().order_by("idVehicle")  
    return render(request,'vehicle.html',{"Vehicles":vehiclelist})

def main(request):
    return render (request, 'main.html')

def qr(request):
    return render (request, 'qr.html')


def deleteVehicle (request, id):
    vehicle=Vehicle.objects.get(id=vehicle.idVehicle)
    vehicle.delete
    return redirect ('')