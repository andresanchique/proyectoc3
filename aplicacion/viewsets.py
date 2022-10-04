from rest_framework import viewsets
from . import models
from . import serializers

class AplicacionViewset(viewsets.ModelViewSet):
    queryset=models.Aplicacion.objects.all()
    serializer_class=serializers.AplicacionSerializer