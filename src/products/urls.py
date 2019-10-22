from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name='products-index'),
    path('about/', views.about,name='products-about'),
    path('xps-webpage/',views.xps,name='xps-webpage'),
    path('latitude-webpage/',views.latitude,name='latitude-webpage'),
    path('alienware-webpage/',views.alienware,name='alienware-webpage'),
    path('inspiron-webpage/',views.inspiron,name='inspiron-webpage'),
    path('xps13-series/',views.xps13_series,name='xps13-series'),
    path('xps15-series/',views.xps15_series,name='xps15-series'),
    path('inspiron15-series/',views.inspiron15_series,name='inspiron15-series'),
    path('inspiron17-series/',views.inspiron17_series,name='inspiron17-series'),
    path('latitude-series/',views.latitude_series,name='latitude-series'),
    path('alienware15-series/',views.alienware15_series,name='alienware15-series'),
    path('alienware17-series/',views.alienware17_series,name='alienware17-series'),
    path('cart',views.cart,name='cart'),
    path('payment-user',views.payment1,name='payment-user'),
    path('payment-pay',views.payment2,name='payment-pay'),
    path('payment-order',views.payment3,name='payment-order'),




    #path('cart/<int:pid>',views.alienware17_series,name='alienware17-series'),
    





    


]
