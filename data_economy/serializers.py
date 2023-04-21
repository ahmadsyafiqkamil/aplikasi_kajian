from rest_framework import serializers
from .models import *


class AktifitasDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AktifitasData
        fields = '__all__'
