from django.db import models
from .acordo import Acordo


class Parcela(models.Model):

	acordo = models.ForeignKey(Acordo,related_name='parcela',on_delete = models.CASCADE)
	valor_parcela = models.FloatField()
	data_vencimento = models.DateField()
	valor_pago = models.FloatField(null=True)
	data_pagamento = models.DateField(null=True)
	status_parcela = models.CharField(max_length=200,default="Não Paga")


