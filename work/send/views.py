from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics
from .models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

class HeaderView(APIView):
    def get(self,*args,**kwargs):
        name = Header.objects.all()
        serializer = HeaderSerializers(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class InformationView(APIView):
    def get(self,*args,**kwargs):
        name = Information.objects.all()
        serializer = InformationsSerializers(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class ConfereceView(APIView):
    def get(self,*args,**kwargs):
        name = ConfereceView.objects.all()
        serializer = Conference(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class AdsView(APIView):
    def get(self,*args,**kwargs):
        name = Ads.objects.all()
        serializer = AdsSerializers(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class CommitetView(APIView):
    def get(self,*args,**kwargs):
        name = Commitet.objects.all()
        serializer = CommitetSerializers(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class EventView(APIView):
    def get(self,*args,**kwargs):
        name = Event.objects.all()
        serializer = EventSerializers(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class DonatView(APIView):
    def get(self,*args,**kwargs):
        name = Donat.objects.all()
        serializer = DonatSerializers(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class RegizView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = RegisSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer,status=status.HTTP_201_CREATED)
