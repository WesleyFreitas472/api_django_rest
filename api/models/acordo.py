from django.db import models
from .cliente import Cliente
from django.db.models.signals import pre_save

class Acordo(models.Model):
	
	data_acordo = models.DateField()
	valor_original = models.FloatField()
	contratante = models.ForeignKey(Cliente,on_delete=models.CASCADE)
	valor_acordado = models.FloatField()
	desconto = models.FloatField()

	class Meta:
		db_table = "acordo"


	
