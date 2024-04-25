from django.urls import path, include
from pays import views as payViews

urlpatterns = [
    path('pse/', payViews.pse, name='pse'),
    path('generateQr/', payViews.generateQr, name='qr'),
    path('validatePay/', payViews.validatePay, name='validatePay'),
]
