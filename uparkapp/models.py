from django.db import models
from .choices import *
from django.contrib.auth.models import User


# Create your models here.


class Vehicle(models.Model):
    idVehicle = models.AutoField(primary_key=True)
    type =  models.CharField(max_length=20)
    rate = models.IntegerField()
    
    def __str__(self):
        texto = "{0}({1})"
        return texto.format(self.type,self.rate)
    

class Person (models.Model):
    idPerson = models.AutoField(primary_key=True)
    documentId = models.CharField(max_length=20, unique= True, null=False, blank=False)
    firstName = models.CharField(max_length=50, null=False, blank=False)
    lastName = models.CharField(max_length=50, null=False, blank=False)
    phone  = models.CharField(max_length=10, null=False, blank=False)
    mail =  models.CharField(max_length=100, unique = True, null=False, blank=False)
    dateOfBirth = models.DateField(null=False, blank=False)
    personType = models.CharField(max_length=1, choices=person_type, null=False, blank=False)
    password = models.CharField(max_length=500, null=False, blank=False)
    #images = models.ImageField(upload_to = 'movie/images/')

    def __str__(self):
        texto = "{0}: {1} {2} - {3}"
        return texto.format(self.idPerson,self.firstName, self.lastName, self.personType)
    
class Card (models.Model):
    idCard = models.AutoField(primary_key=True)
    idPerson= models.ForeignKey(Person, null=False, on_delete=models.CASCADE)
    balance = models.IntegerField()
    status = models.CharField(max_length=1, default='A', choices=card_status)

    def __str__(self):
        texto = "{0}: ({1})"
        return texto.format(self.idCard,self.balance)
    
class Pay(models.Model):
    idPay = models.AutoField(primary_key=True)
    idPerson = models.ForeignKey(Person, null=False, on_delete=models.CASCADE)
    idVehicle = models.ForeignKey(Vehicle, null=True, on_delete=models.CASCADE)
    transactionValue = models.IntegerField()
    cusCod = models.CharField(max_length=7, null=False)
    date = models.DateTimeField()
    #qrCode =  models.ImageField()

    def __str__(self):
        texto = "{0} - {1}"
        return texto.format(self.cusCod,self.transactionValue)
