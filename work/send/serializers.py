from rest_framework import serializers
from .models import *

class HeaderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = '__all__'

class InformationsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'

class ConferenceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = '__all__'

class AdsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = '__all__'

class CommitetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Commitet
        fields = '__all__'

class EventSerializers(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class DonatSerializers(serializers.ModelSerializer):
    class Meta:
        model = Donat
        fields = '__all__'

class RegisSerializers(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'
