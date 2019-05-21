from __future__ import unicode_literals

from django.db import models
from .estado import Estado
from .regional import Regional

class Cidade(models.Model):

	nome = models.CharField(max_length=200, null=True)
	estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
	regiao = models.ForeignKey(Regional, on_delete=models.CASCADE)

	class Meta:
		db_table = 'cidade'