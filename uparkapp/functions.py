import qrcode
from datetime import datetime
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
