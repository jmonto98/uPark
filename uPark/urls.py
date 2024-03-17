"""
URL configuration for uPark project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from uparkapp import views as appViews
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', appViews.main),
    path('addCard/',appViews.addCard),
    path('addPerson/',appViews.addPerson),
    path('addVehicle/',appViews.addVehicle),
    path('admin/', appViews.admin),
    path('adminuser/', appViews.adminuser),
    path('card/',appViews.card),
    path('deleteVehicle/<idVehicle>', appViews.deleteVehicle, name="deleteVehicle"),
    path('editarCard/',appViews.editarCard),
    path('editarVehicle/',appViews.editarVehicle),
    path('editCard/<idCard>', appViews.editCard, name="editcard"),
    path('editVehicle/<idVehicle>',appViews.editVehicle),
    path('errors/', appViews.errors),
    path('generateQr/', appViews.generateQr, name="qr"),
    path('validatePay/', appViews.validatePay),
    path('login/', appViews.login),
    path('main', appViews.main),
    path('manage/', admin.site.urls),#Administrador del proyecto django
    path('pse/', appViews.pse),
    path('reportVehicle/',appViews.reportVehicle),
    path('vehicle/', appViews.vehicle, name="vehicle"),
    path('welcome/',appViews.welcome, name="Welcome")
]
