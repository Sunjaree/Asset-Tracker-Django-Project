
from django.contrib import admin
from django.urls import path, include
from tracker_app import views

urlpatterns = [
    
    path('', views.index, name='tracker_app'),
    
]
