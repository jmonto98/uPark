from django.db import models
from .choices import person_type
from django.contrib.auth.models import User


# Create your models here.

class Card (models.Model):
    idCard = models.AutoField(primary_key=True)
    #idPerson = models.ForeignKey(Person, null=False, on_delete=models.CASCADE)
    balance = models.IntegerField()

    def __str__(self):
        texto = "{0}: ({1})"
        return texto.format(self.idCard,self.balance)

class Vehicle(models.Model):
    idVehicle = models.AutoField(primary_key=True)
    type =  models.CharField(max_length=20)
    rate = models.IntegerField()
    
    def __str__(self):
        texto = "{0}({1})"
        return texto.format(self.type,self.rate)
    

class Person (models.Model):
    idPerson = models.AutoField(primary_key=True)
    idCard = models.ForeignKey(Card, null=False, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    phone  = models.CharField(max_length=10)
    mail =  models.CharField(max_length=100)
    dateOfBirth = models.DateField()
    personType = models.CharField(max_length=10, choices=person_type)
    password = models.CharField(max_length=15, null=False, blank=False)
    #images = models.ImageField(upload_to = 'movie/images/')

    def __str__(self):
        texto = "{0}: {1} {2} - {3}"
        return texto.format(self.idPerson,self.firstName, self.lastName, self.personType)
class Pay(models.Model):
    idPay = models.AutoField(primary_key=True)
    idPerson = models.ForeignKey(Person, null=False, on_delete=models.CASCADE)
    idVehicle = models.ForeignKey(Vehicle, null=False, on_delete=models.CASCADE)
    transactionValue = models.IntegerField()
    cusCod = models.CharField(max_length=7, null=False)
    date = models.DateTimeField()

    def __str__(self):
        texto = "{0} - {1}"
        return texto.format(self.cusCod,self.transactionValue)
