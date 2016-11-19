from django.shortcuts import *
from rest_framework import viewsets
from .models import *
from .serializers import *

def inicia(request):
    return render_to_response("base.html")

def insere_dentista(request):
    pass

#------------ REST API app_clinica ----------------#
class DentistaViewSet(viewsets.ModelViewSet):
    queryset = Dentista.objects.all()
    serializer_class = DentistaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

