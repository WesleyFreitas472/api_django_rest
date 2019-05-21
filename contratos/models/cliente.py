from __future__ import unicode_literals

from django.db import models
from .empresa import Empresa

class Cliente(models.Model):
	nome = models.CharField(max_length=200)
	empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)

	class Meta:
		db_table = 'cliente'

