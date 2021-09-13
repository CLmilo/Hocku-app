from django.shortcuts import render
from django.urls import path
from R_Grados import views

urlpatterns = [
    path('RG', views.RViews),
]
