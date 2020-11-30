from django.db import models

class Cliente(models.Model):
    nome = models.CharField("Nome", max_length=120)
    endereco = models.CharField("Endereço",max_length=500)
    email = models.EmailField("Email")
    data_cadastro = models.DateField(auto_now_add=True)