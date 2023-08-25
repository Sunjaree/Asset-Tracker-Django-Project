
from django.contrib import admin
from django.urls import path, include
from tracker_app import views

urlpatterns = [
    
    path('', views.index, name='tracker_app'),
    path('signup', views.handle_signup, name='handle_signup'),
    path('login', views.handle_login, name='handle_login'),
    path('logout', views.handle_logout, name='handle_logout'),
    path('add_employee', views.add_employee, name='add_employee'),
    path('add_assets', views.add_assets, name='add_assets'),
    path('assign_assets', views.assign_assets, name='assign_assets'),
    path('view_assigned_assets', views.view_assigned_assets, name='view_assigned_assets')
    
]
