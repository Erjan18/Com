from rest_framework import serializers
from .models import *

class RegisSerializers(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'
