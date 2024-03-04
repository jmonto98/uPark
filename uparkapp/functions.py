import qrcode
import time
import random

def cusGen():
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTVWXYZ'
    cus = ''
    for _ in range(7):
        cus += random.choice(chars)

    return cus


def qrGenerate(cus, vehicleType):
    input = 'uPark-tiquete de '+ vehicleType + '-' + time.strftime("%c") + '-' + cus
    
    qr = qrcode.QRCode(version=1,box_size=10,border=5)

    qr.add_data(input)
    qr.make(fit=True)

    img=qr.make_image(fill='black',back_color='white')
    img.save('../uPark/media/qrcodes/'+vehicleType+'_'+cus+'QR.png')
    print(input)

#codigo = cusGen()
qrGenerate(cusGen(), 'carro')
