from django.shortcuts import render
from uparkapp.models import *
from uparkapp.functions import *



def main(request):
    vehiclelist=Vehicle.objects.all().order_by("idVehicle") 
    pays = paysCon()
    tickets = paperSaved()    
    return render (request, 'main.html',{"trees":tickets,"watts":wattsSaved, "pays":pays, "Vehicles":vehiclelist})

def registration(request):
    return render (request, 'registration.html')

def pse(request):    
    return render (request, 'errors.html',{"error":"Vengo de Accounts"})