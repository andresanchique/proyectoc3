from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Aplicacion

class AplicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Aplicacion
        fields='__all__'