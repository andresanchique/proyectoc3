from django.urls import path
from aplicacion.viewfrontend import principal
from aplicacion.views import EmpleadoView
from aplicacion.views import EmpresaView
from aplicacion.views import MovimientosView

urlpatterns= [
    path('Empleado/',EmpleadoView.as_view(),name='Listar'),
    path('Empleado/<str:usuario>',EmpleadoView.as_view(),name='Buscar'),
    path('Empresa/',EmpresaView.as_view(),name='Listar'),
    path('Empresa/<str:codigo>',EmpresaView.as_view(),name='Buscar'),
    path('Movimientos/',MovimientosView.as_view(),name='Listar'),
    path('Movimientos/<str:codigo_mov>',MovimientosView.as_view(),name='Buscar'),
    path('', principal, name="index")
]