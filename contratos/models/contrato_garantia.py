from __future__ import unicode_literals

from django.db import models
from .contrato import Contrato
from .garantia import Garantia

class ContratoGarantia(models.Model):
	garantia = models.ForeignKey(Garantia,on_delete=models.CASCADE)
	contrato = models.ForeignKey(Contrato,on_delete=models.CASCADE)

	class Meta:
		db_table = 'contrato_garantia'


