from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from .models import *
#Manejo de libros de excel
from openpyxl import Workbook


# Create your views here.

def login(request):
    #return HttpResponse('<h1>Welcome to Upark login</h1>')
    return render (request, 'login.html')

def admin(request):
    return render (request, 'admin.html')

def user(request):
    return render (request, 'user.html')

def card(request):
    return render (request, 'card.html')

def visitor(request):
    return render (request, 'visitor.html')

def vehicle(request):
    vehiclelist=Vehicle.objects.all().order_by("idVehicle")  
    return render(request,'vehicle.html',{"Vehicles":vehiclelist})

def main(request):
    return render (request, 'main.html')

def pse(request):
    return render (request, 'pse.html')

def generateQr(request):
    return render (request, 'generateQr.html')

def addVehicle (request):
    type = request.POST ['type']
    rate = request.POST ['rate']    
    vehicle = Vehicle.objects.create(type=type, rate=rate)
    vehicle.save()
    return redirect ('/vehicle')

def editVehicle (request, idVehicle):
    vehicle = Vehicle.objects.get(idVehicle=idVehicle)
    return render (request, "editVehicle.html",{"vehicle" : vehicle})

def editarVehicle (request):
    idVehicle = request.POST ['idVehicle']
    type = request.POST ['type']
    rate = request.POST ['rate'] 
    vehicle = Vehicle.objects.get(idVehicle=idVehicle)
    vehicle.type = type
    vehicle.rate = rate
    vehicle.save()
    return redirect ('/vehicle')    

def deleteVehicle (request, idVehicle):
    vehicle = Vehicle.objects.get(idVehicle=idVehicle)
    vehicle.delete()
    return redirect ('/vehicle')

def addPerson (request):
    firstName = request.POST ['firstName']
    lastName = request.POST ['lastName']
    phone  = request.POST ['phone']
    mail =  request.POST ['mail']
    dateOfBirth = request.POST ['dateOfBirth']
    personType = request.POST ['personType']
    person = Person.objects.create(firstName=firstName,
                                lastName=lastName,
                                phone=phone,
                                mail=mail,
                                dateOfBirth=dateOfBirth,
                                personType=personType)
    person.save()
    return redirect ('/user')

def addCard (request):
    #idCard = request.POST ['idCard']
    balance = request.POST ['balance']
    card = Card.objects.create (balance = balance)
    card.save()
    return redirect ('/card')
    

    

#"Pendiente-en construccion"
def reportVehicle(request):
    vehicle = Vehicle.objects.all()
    wb = Workbook()
    ws = wb.active
    ws['A1'] = 'VEHICLE LIST'
    #Cabezera de reporte
    ws.merge_cells('A1:C1')
    ws['A3'] = 'Id Vehicle'
    ws['B3'] = 'Type Vehicle'
    ws['C3'] = 'Rate'
    
    cont = 5
    for vechicle in vechicle:
        ws.cell(row = cont, column =2).value = vehicle.idVehicle
        ws.cell(row = cont, column =3).value = vehicle.type
        ws.cell(row = cont, column =4).value = vehicle.rate
        cont += 1
    fileName= "List_Vechicle_Upark.xlsx"
    response = HttpResponse(content_type = "applications/ms-excel")
    content = "attachment"; filename={0},format(fileName)
    response['Content-Disposition'] = content
    wb.save(response)
    return (response)
            
        
    
 
    

            
    
    