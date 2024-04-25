from django.shortcuts import render
from uparkapp.models import *



def main(request):
    vehiclelist=Vehicle.objects.all().order_by("idVehicle")     
    return render (request, 'main.html',{"Vehicles":vehiclelist})

def registration(request):
    return render (request, 'registration.html')

def pse(request):    
    return render (request, 'errors.html',{"error":"Vengo de Accounts"})