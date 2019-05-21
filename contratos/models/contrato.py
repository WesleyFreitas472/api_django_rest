from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from .carteira import Carteira
from .agencia import Agencia
from .cliente import Cliente
from .pessoa import Endereco

class Contrato(models.Model):
	num_contrato = models.CharField(max_length=200)
	carteira = models.ForeignKey(Carteira,on_delete=models.CASCADE)
	agencia = models.ForeignKey(Agencia,on_delete=models.CASCADE)
	cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)

	data_contrato = models.DateField(null=True)

	valor_contrato = models.FloatField()
	valor_corrigido = models.FloatField()

	data_cadastro = models.DateField(timezone.now())
	endereco = models.ForeignKey(Endereco,on_delete=models.CASCADE)


	class Meta:
		db_table = 'contrato'


class ParcelaContrato(models.Model):
	data_vencimento = models.DateField()
	contrato = models.ForeignKey(Contrato,on_delete=models.CASCADE)
	data_cadastro = models.DateField(default=timezone.now())
	valor_parcela = models.FloatField()
	valor_corrigido = models.FloatField(null=True)


	class Meta:
		db_table = 'parcela_contrato'