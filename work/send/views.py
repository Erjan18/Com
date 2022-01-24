from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics
from .models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

class RegizView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = RegisSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer,status=status.HTTP_201_CREATED)