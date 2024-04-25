from django.shortcuts import render
from uparkapp.models import *
from uparkapp.functions import *
from datetime import datetime


def generateQr(request):
    return render(request,'generateQr.html')

def pse(request):    
    try:
        vehicle=Vehicle.objects.get(idVehicle = request.POST ['type'])
        if vehicle.idVehicle != 1:
            return render(request, "pse.html",{"vehicle": vehicle.type, "idVehicle": vehicle.idVehicle, "rate": vehicle.rate, "idPerson":request.POST ['idPerson']})
        else:
            return render(request, "pse.html",{"vehicle": vehicle.type, "idVehicle": vehicle.idVehicle, "rate": request.POST ['rate'], "idPerson":request.POST ['idPerson']})
    except:
        return render(request, "main.html")
    

def validatePay(request):
    try:
        cus = cusGen()
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        person = Person.objects.get(idPerson = request.POST ['idPerson'])
        vehicle = Vehicle.objects.get(idVehicle = request.POST ['idVehicle'])
        
        pay = Pay.objects.create(transactionValue = request.POST ['_rate'],
                                 idPerson = person,
                                 idVehicle = vehicle,
                                 cusCod = cus,
                                 date = now)
        
        if vehicle.idVehicle != 1:
            qr = qrGenerate(cus, vehicle.type, now)
            #pay.save()
            return render (request, 'generateQr.html', {"qr":qr})
        else:            
            card = Card.objects.get(idPerson = person.idPerson)
            pay.idPerson = card.idPerson
            card.balance = card.balance + int(request.POST['_rate'])
            card.save()
            pay.save()
            paylist=Pay.objects.filter(idPerson_id= person.idPerson).order_by("idPay")  
            return render(request, "welcome.html",{"resulPerson": person.firstName, "idPerson":person.idPerson, "resulCard": card.balance, "Viewpay":paylist})     
    except:
        return render (request, 'errors.html',{"error": "Something went wrong durig the transaction"})