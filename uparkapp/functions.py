import qrcode
import datetime as tempo
from datetime import datetime
from datetime import timedelta
import random
from uPark import settings 
from .models import *
from werkzeug.security import generate_password_hash, check_password_hash 


def cusGen():
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTVWXYZ'
    cus = ''
    for _ in range(7):
        cus += random.choice(chars)

    return cus


def qrGenerate(cus, vehicleType, now):
    #now = datetime.strptime(now, "%Y-%m-%d %H:%M:%S")
    #input = 'uPark- '+ vehicleType + ' Ticket -' + now.strftime('%d%m%Y_%H%M%S') + '-' + cus
    input = 'uPark- '+ vehicleType + ' Ticket -' + now + '-' + cus
    nameQr = vehicleType+'_'+cus+'.png'
    qr = qrcode.QRCode(version=1,box_size=10,border=5)

    qr.add_data(input)
    qr.make(fit=True)

    img=qr.make_image(fill='black',back_color='white')
    #img.save('./uPark/media/qrcodes/'+ nameQr)
    img.save(settings.QR_ROOT + nameQr)
    #print(input)
    return (nameQr)

def encryptPwd(pwd):
    pwd = generate_password_hash(pwd, 'pbkdf2:sha1', 8)
    return (pwd)

def decryptPwd(encripted, pwd):   
    return check_password_hash(encripted, pwd)


def randomDate():
    start_date = datetime(2024, 1, 1, 6, 00, 00)
    end_date   = datetime(2024, 5, 7, 22, 00, 00)

    num_days   = (end_date - start_date).days
    rand_days   = random.randint(1, num_days)
    random_date = start_date + tempo.timedelta(days=rand_days,hours=random.randint(1,24),minutes=random.randint(0,59),seconds=random.randint(0,59))
    return(random_date)


def masivePays(x):
    for i in range(x) :
        now = randomDate()
        idPerson = random.randint(1,5)
        person = Person.objects.get(idPerson = idPerson)
        
        cus = cusGen()
        if (idPerson == 1):
            idVehicle = random.randint(2,4)
            vehicle = Vehicle.objects.get(idVehicle = idVehicle)
            if (idVehicle == 2):
                value = 7000
            elif (idVehicle == 3):
                value = 5000
            else:
                value = 3500
        else:
            idVehicle = 1
            value = random.randrange(1000, 50000, 1000)
            vehicle = Vehicle.objects.get(idVehicle = idVehicle)
        
        pay = Pay.objects.create(transactionValue = value,
                                    idPerson = person,
                                    idVehicle = vehicle,
                                    cusCod = cus,
                                    date = now)
        pay.save()

    return("Carga Masiva exitosa")

def genFlatFile(pays):
    file = open("./uPark/media/files/flatFile.txt", "w")
    for p in pays:
        person = Person.objects.get(idPerson = p.idPerson_id)
        file.write(str(p.idPay)+";"+str(p.transactionValue)+";"+str(p.cusCod)+";"+str(p.date.strftime('%Y-%m-%d %H:%M:%S'))+";"+str(person.documentId)+";"+str(p.idVehicle_id)+";"+ "\n")

    file.close()
    return (file)

def paperSaved():
    pays = paysCon()*0.2
    tickets = Pay.objects.filter(idPerson_id = 1).count() + pays
    tickets = round(tickets/8000,3)
    return(tickets)

def wattsSaved():
    end_date = datetime.today()
    start_date = datetime(2024, 1, 1, 6, 00, 00)
    num_days   = (end_date - start_date).days
    
    watts = num_days * (600 * 0.85)
    return(watts)

def paysCon():
    pays = Pay.objects.count()
    return(pays)