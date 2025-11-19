from django.contrib import admin
from django.urls import path
from zyra_app import views


urlpatterns=[
    path('',views.viewhome,name='homepage'),
    
]