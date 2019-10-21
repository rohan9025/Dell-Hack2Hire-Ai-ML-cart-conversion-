from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home,name='products-home'),
    path('about/', views.about,name='products-about'),
    path('xps-webpage/',views.xps,name='xps-webpage')
]
