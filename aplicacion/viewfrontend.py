import json
#from urls import response
from django.shortcuts import render, redirect
from django.http import HttpResponse
#import requests

from aplicacion.models import Empresas

def principal(request):
    return render(request, "index.html")

'''def ConsultaEmpresa(request):
    response=requests.get('http://localhost:8000/aplicacion/Empresa')
    Empresas=response.json()
    print(Empresas)
    return render(request, "empresa.html",Empresas)

def crearEmpresa(request):
    dato=request.POST['isbn']
    response=requests.get('http://localhost:8000/aplicacion/Empresa/'+dato)
    Empresas=response.json()
    print(Empresas)
    return render(request, "empresa.html",Empresas)'''