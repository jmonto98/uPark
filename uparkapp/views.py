from .functions import *
from typing import Any
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.exceptions import *
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

#Manejo de libros de excel
from openpyxl import Workbook


# Create your views here.

def main(request):
    vehiclelist=Vehicle.objects.all().order_by("idVehicle") 
    return render (request, 'main.html',{"Vehicles":vehiclelist})

def login(request):
    #return HttpResponse('<h1>Welcome to Upark login</h1>')
    if request.method == 'GET':
        return render(request, 'login.html',{
            'form':AuthenticationForm
        })
    else:  
        user = authenticate(
            request, username=request.POST['username'],password=request.POST['password'])
        if user is None:

            return render(request, 'login.html',{
                'form':AuthenticationForm,
                'error':'username or password is incorrect'
            })
        else:
           
         login(request,user)
         return redirect('admin')  
        

def welcome(request):
    return render (request, 'welcome.html')

def admin(request):
    return render (request, 'admin.html')

def prueba(request):
    return render (request, 'prueba.html')

def adminuser(request):
    return render (request, 'adminuser.html')

def card(request):
    cardList= Card.objects.all().order_by("idCard")
    return render (request, 'card.html',{"Card": cardList})

def visitor(request):
    return render (request, 'visitor.html')

def vehicle(request):
    vehiclelist=Vehicle.objects.all().order_by("idVehicle")  
    return render(request,'vehicle.html',{"Vehicles":vehiclelist})

def pse(request):
    vehicle=Vehicle.objects.get(idVehicle = request.POST ['type'])
    return render(request, "pse.html",{"vehicle": vehicle.type, "rate": vehicle.rate})


def generateQr(request):
    vehicle = 'avion'#request.POST ['vehicle']
    qrGenerate(cusGen(),vehicle)
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
        pwd = request.POST ['password']
        phone  = request.POST ['phone']
        mail =  request.POST ['mail']
        dateOfBirth = request.POST ['dateOfBirth']
        personType = request.POST ['personType']
        person = Person.objects.create(firstName=firstName,
                                    lastName=lastName,
                                    password = pwd,
                                    phone=phone,
                                    mail=mail,
                                    dateOfBirth=dateOfBirth,
                                    personType=personType)
        person.save()
        return redirect ('/adminuser')

def addCard (request):
    #idCard = request.POST ['idCard']    
    idPerson = request.POST ['idPerson']
    balance = request.POST ['balance']
    status = request.POST ['status']
    card = Card.objects.create (idPerson_id=idPerson, balance = balance,status=status)
    card.save()
    return redirect ('/card')

def editCard (request, idCard):
    card = Card.objects.get(idCard=idCard)
    return render (request, "editCard.html",{"card" : card})

def editarCard (request):
    idCard = request.POST ['idCard']
    idPerson = request.POST ['idPerson']
    balance = request.POST ['balance']
    status = request.POST ['status']
    card = Card.objects.get(idCard=idCard)
    card.idPerson = idPerson
    card.balance = balance
    card.status = status
    card.save()
    return redirect ('/editcard')    
    
def balance (request):
    data = request.POST ['username']
    person=Person.objects.get (mail=data)
    obj = Card.objects.get(idCard =  data)
    d = (obj.idPerson, obj.balance)
    try:
        return render(request, "welcome.html",{"d": d})
    except ObjectDoesNotExist:
        mensaje = "El objeto que estás buscando no se encuentra en la base de datos."
        return render(request, "welcome.html",{"mensaje":mensaje})
    

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
            
        
    
 
    

            
    
    