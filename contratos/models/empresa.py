from __future__ import unicode_literals

from django.db import models


class Empresa(models.Model):
	nome = models.CharField(max_length=200,unique=True)

	class Meta:
		db_table = 'empresa'