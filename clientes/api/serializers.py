from clientes.models import Cliente
from rest_framework.serializers import ModelSerializer


class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = ["id", "nome", "endereco", "email", "data_cadastro",]