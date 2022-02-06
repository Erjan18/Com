from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('header/',HeaderView.as_view(),name='header'),
    path('info/',InformationView.as_view(),name='info'),
    path('confer/',ConfereceView.as_view(),name='confer'),
    path('ads/',AdsView.as_view(),name='ads'),
    path('commit/',CommitetView.as_view(),name='commit'),
    path('event/',EventView.as_view(),name='event'),
    path('donat/',DonatView.as_view(),name='donat'),
    path('regis/',RegizView.as_view(),name='regis')

]