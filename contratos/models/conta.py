from __future__ import unicode_literals

from django.db import models
from .agencia import Agencia

class Conta(models.Model):
	agencia = models.ForeignKey(Agencia, on_delete=models.CASCADE)
	num = models.CharField(max_length=200)

	class Meta:
		db_table = 'conta'