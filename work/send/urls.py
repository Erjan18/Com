from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('regis/',RegizView.as_view(),name='regis')

]