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
from django.urls import path
from uparkapp import views as appViews


urlpatterns = [
    path('prueba/', appViews.prueba),
    path('', appViews.main),
    path('main/', appViews.main),
    path('manage/', admin.site.urls),#Administrador del proyecto
    path('admin/', appViews.admin),
    path('adminuser/', appViews.adminuser),
    path('card/',appViews.card),
    path('generateQr/', appViews.generateQr),
    path('vehicle/', appViews.vehicle, name="vehicle"),
    path('login/', appViews.login),
    path('pse/', appViews.pse),
    path('addVehicle/',appViews.addVehicle),
    path('editarVehicle/',appViews.editarVehicle),
    path('editVehicle/<idVehicle>',appViews.editVehicle),
    path('deleteVehicle/<idVehicle>', appViews.deleteVehicle, name="deleteVehicle"),
    path('reportVehicle/',appViews.reportVehicle),
    path('addPerson/',appViews.addPerson),
    path('addCard/',appViews.addCard),
    path('mainuniversity/',appViews.mainuniversity)
    
]
