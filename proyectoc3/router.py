from django.db import router
from aplicacion.viewsets import AplicacionViewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register('aplicacion', AplicacionViewset)
