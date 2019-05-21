from __future__ import unicode_literals

from django.db import models

class Garantia(models.Model):
	tipo = models.CharField(max_length=200)
	descricao = models.CharField(max_length=500,null=True)
	marca = models.CharField(max_length=200,null=True)
	placa = models.CharField(max_length=10,null=True)
	renavam = models.CharField(max_length=200,null=True)
	cor = models.CharField(max_length=200,null=True)
	ano_fabricacao = models.IntegerField(null=True)
	ano_modelo = models.IntegerField(null=True)

	class Meta:
		db_table = 'garantia'
