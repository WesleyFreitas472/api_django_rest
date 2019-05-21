from __future__ import unicode_literals

from django.db import models

class Carteira(models.Model):
	numero = models.CharField(max_length=200)
	classificacao = models.CharField(max_length=200)
	descricao = models.CharField(max_length=500)
