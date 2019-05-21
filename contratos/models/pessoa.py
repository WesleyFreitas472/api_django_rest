from django.db import models
from .cidade import Cidade


class Pessoa(models.Model):
	nome = models.CharField(max_length=200)
	cpf_cnpj = models.CharField(max_length=200, null=True)

	class Meta:
		db_table = "pessoa"

class Endereco(models.Model):
	rua = models.CharField(max_length=200,null=True)
	numero = models.IntegerField(null=True)
	complemento = models.CharField(max_length=200,null=True)
	cep = models.IntegerField(max_length=200,null=True)
	bairro = models.CharField(max_length=200,null=True)
	cidade = models.ForeignKey(Cidade,on_delete=models.CASCADE)
	
	class Meta:
		db_table = 'endereco'

class PessoaEndereco(models.Model):
	pessoa = models.ForeignKey(Pessoa,on_delete=models.CASCADE)
	pessoa_endereco = models.ForeignKey(Endereco,on_delete=models.CASCADE)

	class Meta:
		db_table = 'pessoa_endereco'

class Telefone(models.Model):
	choices = (
		('HOT','HOT'),
		('PESSOAL','PESSOAL'),
		('PESSOA_RELACIONADA','PESSOA_RELACIONADA'),
		('COMERCIAL','COMERCIAL'),
	)
	qualificacao = models.CharField(max_length=40,choices=choices)
	numero = models.CharField(max_length=40)
	celular = models.BooleanField()

	def save():
		#verficar se telefone é fixo ou celular
		super().save(self)
