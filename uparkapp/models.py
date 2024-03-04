from django.db import models

from .choices import person_type

# Create your models here.

class Card (models.Model):
    idCard = models.AutoField(primary_key=True)
    #idPerson = models.ForeignKey(Person, null=False, on_delete=models.CASCADE)
    balance = models.IntegerField()

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
    #images = models.ImageField(upload_to = 'movie/images/')

class Pay(models.Model):
    idPay = models.AutoField(primary_key=True)
    idPerson = models.ForeignKey(Person, null=False, on_delete=models.CASCADE)
    idVehicle = models.ForeignKey(Vehicle, null=False, on_delete=models.CASCADE)
    transactionValue = models.IntegerField()
    date = models.DateTimeField()
