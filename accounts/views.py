from django.shortcuts import render
from uparkapp.models import *
from . import views


def main(request):
    vehiclelist=Vehicle.objects.all().order_by("idVehicle")     
    return render (request, 'main.html',{"Vehicles":vehiclelist})