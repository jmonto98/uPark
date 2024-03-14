import qrcode
from datetime import datetime
import random
from uPark import settings 
from .models import *


def cusGen():
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTVWXYZ'
    cus = ''
    for _ in range(7):
        cus += random.choice(chars)

    return cus


def qrGenerate(cus, vehicleType):
    now = datetime.now()
    input = 'uPark-Ticket of '+ vehicleType + '-' + now.strftime('%d%m%Y_%H%M%S') + '-' + cus
    nameQr = vehicleType+'_'+cus+'.png'
    qr = qrcode.QRCode(version=1,box_size=10,border=5)

    qr.add_data(input)
    qr.make(fit=True)

    img=qr.make_image(fill='black',back_color='white')
    #img.save('./uPark/media/qrcodes/'+ nameQr)
    img.save(settings.QR_ROOT + nameQr)
    #print(input)
    return (nameQr)
    
def authenticate(user):
    person = Person.objects.get(mail = user)
    
    if person is None:
        return(0)
    elif person.password == "123456789":
        return (1)
    else:
        return (2)
