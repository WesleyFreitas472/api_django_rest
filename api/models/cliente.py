from django.db import models

class Cliente(models.Model):
	nome = models.CharField(max_length=200,unique=True)
	idade = models.IntegerField()
	altura = models.FloatField()
	profissao = models.CharField(max_length=200,null=True)
	salario = models.FloatField(null=True)

