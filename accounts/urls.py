from django.urls import path
from . import views as accViews

urlpatterns = [
    path('', accViews.main, name='main'),
    path('main', accViews.main, name='main'),
    
]
