from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('createWallet', views.createWallet,name= 'createWallet'),
    path('viewwallets', views.viewWallets, name='viewWallets'),

]