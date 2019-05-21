from __future__ import unicode_literals

from django.db import models

class Estado(models.Model):
	nome = models.CharField(max_length=200,unique=True)
	sigla = models.CharField(max_length=2,unique=True)
	regiao = models.CharField(max_length=50)

	class Meta:
		unique_together = ['nome','sigla']
		db_table = 'estado'
