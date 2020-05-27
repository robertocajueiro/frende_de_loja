from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100, help_text='Digite o nome do cliente')
    cpf = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20, help_text='Informe o contato do cliente')
