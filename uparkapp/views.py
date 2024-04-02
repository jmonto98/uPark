import re
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
from django.db.models import Max
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
import matplotlib.pyplot as plt
import matplotlib
import io
import urllib, base64
from datetime import datetime

#Manejo de libros de excel
from openpyxl import Workbook


# Create your views here.

def main(request):
    vehiclelist=Vehicle.objects.all().order_by("idVehicle")     
    return render (request, 'main.html',{"Vehicles":vehiclelist})

def login(request):
    return render(request, 'login.html')

def admin(request):
    return render (request, 'admin.html')

def prueba(request):
    return render (request, 'prueba.html')

def adminuser(request):
    return render (request, 'adminuser.html')

def card(request):
    cardList= Card.objects.select_related ('idPerson').all()    
    return render (request, 'card.html',{"Card": cardList})

def visitor(request):
    return render (request, 'visitor.html')

def vehicle(request):
    vehiclelist=Vehicle.objects.all().order_by("idVehicle")  
    return render(request,'vehicle.html',{"Vehicles":vehiclelist})

def generateQr(request):
    return render(request,'generateQr.html')

def pse(request):    
    try:
        vehicle=Vehicle.objects.get(idVehicle = request.POST ['type'])
        if vehicle.idVehicle != 0:
            return render(request, "pse.html",{"vehicle": vehicle.type, "idVehicle": vehicle.idVehicle, "rate": vehicle.rate, "idPerson":request.POST ['idPerson']})
        else:
            return render(request, "pse.html",{"vehicle": vehicle.type, "idVehicle": vehicle.idVehicle, "rate": request.POST ['rate'], "idPerson":request.POST ['idPerson']})
    except:
        return render(request, "main.html")

def errors(request):
    return render (request, 'errors.html',{"error": request.POST['error']})

def validatePay(request):
    try:
        cus = cusGen()
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        person = Person.objects.get(idPerson = request.POST['idPerson'])
        vehicle = Vehicle.objects.get(idVehicle = request.POST ['idVehicle'])
        
        pay = Pay.objects.create(transactionValue = request.POST ['_rate'],
                                 idPerson = person,
                                 idVehicle = vehicle,
                                 cusCod = cus,
                                 date = now)
        
        if vehicle.idVehicle != 0:
            qr = qrGenerate(cus, vehicle.type, now)
            pay.save()
            return render (request, 'generateQr.html', {"qr":qr})
        else:            
            card = Card.objects.get(idPerson = person.idPerson)
            pay.idPerson = card.idPerson
            card.balance = card.balance + int(request.POST['_rate'])
            card.save()
            pay.save()
            return render(request, "welcome.html",{"resulPerson": person.firstName, "idPerson":person.idPerson, "resulCard": card.balance})
            
    except:
        return render (request, 'errors.html',{"error": "Algo salío mal durante la transacción"})

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
    try:        
        firstName = request.POST ['firstName']
        lastName = request.POST ['lastName']
        pwd = encryptPwd(request.POST ['password'])
        #pwd = request.POST ['password']
        phone  = request.POST ['phone']
        mail = str.replace(request.POST ['mail'].lower(), ' ', '')
        dateOfBirth = request.POST ['dateOfBirth']
        personType = request.POST ['personType']
        person = Person.objects.create(firstName=firstName,
                                    lastName=lastName,
                                    password = pwd,
                                    phone=phone,
                                    mail=mail,
                                    dateOfBirth=dateOfBirth,
                                    personType=personType)        
        
        lastId = Person.objects.aggregate(idPerson = models.Max('idPerson'))
        cont = lastId['idPerson']
        card=Card.objects.create(idPerson_id= cont,
                                 balance= '0',                                 
                                 status='A')
        person.save()
        card.save()
        return redirect ('/adminuser')
    except:
        user = Person.objects.get(mail = mail)
        if user:
            return render (request, 'errors.html',{"error": "The email is already assigned to another person"})
        else:
            return render (request, 'errors.html',{"error": "Something went wrong!"})

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
    
def welcome (request):
    try:
        person = Person.objects.get(mail = request.POST['username'])
        #return render(request, "Errors.html",{"error":person.password})
    except:
        return render(request, "login.html",{"error": "usuario no existe"})
    
    if (decryptPwd(person.password, request.POST['password'])):
    #if person.password == request.POST['password']:
        card = Card.objects.get(idPerson =  person.idPerson)
        if person.personType == 'A':
           return render(request, "Admin.html")
        else:
            return render(request, "welcome.html",{"resulPerson": person.firstName, "idPerson":person.idPerson, "resulCard": card.balance})
    else:
        return render(request, "login.html",{"error": "Contraseña inválida"})

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

def Viewpay(request):
    paylist=Pay.objects.filter(idPerson_id=request.GET ['idPerson_id']).order_by("idPay")  
   
    return render(request,'welcome.html',{"welcome":paylist})

def statistics_view(request): 
    matplotlib.use('Agg') 
    # Obtener todas los pagos 
    all_pays = Pay.objects.all() 
    
    # Crear un diccionario para almacenar la cantidad de pagos 
    pay_counts_by_date = {} 
    pay_counts_by_vehicle = {} 
    
    # Filtrar los pagos por fecha y contar la cantidad de pagos por fecha 
    for pay in all_pays:

        date = pay.date
        date = date.strftime("%d/%m/%Y")
        if date in pay_counts_by_date: 
            pay_counts_by_date[date] += 1 
        else: 
            pay_counts_by_date[date] = 1  

        #Captura datos por Vehiculo
        vehicle = pay.idVehicle

        if vehicle.type in pay_counts_by_vehicle: 
            pay_counts_by_vehicle[vehicle.type] += 1 
        else: 
            pay_counts_by_vehicle[vehicle.type] = 1    
        
    # Ancho de las barras 
    bar_width = 0.5 
    # Posiciones de las barras 
    bar_positions = range(len(pay_counts_by_date)) 
    
    # Crear la gráfica de barras 
    plt.bar(bar_positions, pay_counts_by_date.values(), width=bar_width, align='center', color ='green') 
    
    # Personalizar la gráfica 
    plt.title('Pay per Date') 
    plt.xlabel('Date') 
    plt.ylabel('Number of pay') 
    plt.xticks(bar_positions, sorted(pay_counts_by_date.keys()), rotation=90) 

    for i, label in enumerate(pay_counts_by_date.values()):
        plt.annotate(label, (i-0.2, (label/2)))
    
    # Ajustar el espaciado entre las barras 
    plt.subplots_adjust(bottom=0.3) 
    
    # Guardar la gráfica en un objeto BytesIO
    buffer = io.BytesIO() 
    plt.savefig(buffer, format='png') 
    buffer.seek(0) 
    plt.close() 
    
    # Convertir la gráfica a base64 
    image_png = buffer.getvalue() 
    buffer.close() 
    graphic = base64.b64encode(image_png) 
    graphic = graphic.decode('utf-8') 

    #---Creacion grafica por vehiculo----#
    bar_width = 0.5 
    # Posiciones de las barras 
    bar_positions = range(len(pay_counts_by_vehicle)) 
    
    # Crear la gráfica de barras 
    plt.bar(bar_positions, pay_counts_by_vehicle.values(), width=bar_width, align='center') 
    
    # Personalizar la gráfica 
    plt.title('Pay per Vehicle') 
    plt.xlabel('Vehicle') 
    plt.ylabel('Number of pay')
    plt.xticks(bar_positions, sorted(pay_counts_by_vehicle.keys()), rotation='vertical')

    for i, label in enumerate(pay_counts_by_vehicle.values()):
        plt.annotate(label, (i-0.05, (label/2)))
    
    # Ajustar el espaciado entre las barras 
    plt.subplots_adjust(bottom=0.3) 
    
    # Guardar la gráfica en un objeto BytesIO
    buffer = io.BytesIO() 
    plt.savefig(buffer, format='png') 
    buffer.seek(0) 
    plt.close() 
    
    # Convertir la gráfica a base64 
    image_png = buffer.getvalue() 
    buffer.close() 
    graphicG = base64.b64encode(image_png) 
    graphicG = graphicG.decode('utf-8') 
    
    # Renderizar la plantilla 
    # admin.html con la gráfica 
    return render(request, 'admin.html', {'graphic': graphic,'graphicG': graphicG})


            
    
    