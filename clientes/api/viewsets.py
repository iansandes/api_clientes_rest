from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from clientes.models import Cliente
from .serializers import ClienteSerializer
from rest_framework.response import Response

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer