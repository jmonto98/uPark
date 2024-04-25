from django.urls import path, include
from accounts import views as accViews

urlpatterns = [
    path('', include('pays.urls')),
    path('', accViews.main, name='main'),
    path('main/', accViews.main, name='main'),
    path('registration/', accViews.registration, name='registration'),
    
]
